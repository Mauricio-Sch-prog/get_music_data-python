import os

from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
 
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


getSongsDetails = types.FunctionDeclaration(
    name='get_songs-details',
    description='Extract metadata from music filenames.',
    parameters_json_schema={
        'type': 'object',
        'properties': {
            'songs': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'file': {'type': 'string', 'description': 'Original filename'},
                        'title': {'type': 'string', 'description': 'Song title'},
                        'author': {'type': 'string', 'description': 'Band/Artist'},
                        'genre': {'type': 'string', 'description': 'Genre'}
                    },
                    'required': ['file', 'title', 'author', 'genre']
                }
            }
        }
    }
)

sys_instr = ("You are a music metadata expert. For every filename provided, "
                 "research the song to find its official title, artist, and genre. "
                 "You MUST call the get_songs_details function for EVERY file in the list. "
                 "Do not skip any files.")

tool = types.Tool(function_declarations=[getSongsDetails])
search_tool = types.Tool(google_search=types.GoogleSearch())





def aiQuery(contents, **config_options):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=contents,
        config=types.GenerateContentConfig(**config_options),
    )
    return response


def putAitoWork(musicList):
    formatted_list = ", ".join(musicList)
    
    research_response = aiQuery(
        f"Research the following music files and find their official title, artist, and genre: {formatted_list}",
        tools = [search_tool]
    )
    
    
    final_response = aiQuery(
        f"Based on this research: {research_response.text}. "
        f"Now, call get_songs_details for these specific files: {formatted_list}",
        system_instruction=sys_instr,
            tools=[tool],
            tool_config=types.ToolConfig(
                function_calling_config=types.FunctionCallingConfig(
                    mode='ANY',
                )
            )
    )

    response = False

    for part in final_response.candidates[0].content.parts:
        if part.function_call:
            response = part.function_call.args['songs']

    client.close()
    return response