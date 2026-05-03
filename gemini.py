import os

from google import genai
from google.genai import types
from dotenv import load_dotenv

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from google.api_core import exceptions
from google.genai import errors

 
load_dotenv()



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
                        'artist': {'type': 'string', 'description': 'Band/Artist'},
                        'album': {'type': 'string', 'description': 'Song album'},
                        'genre': {'type': 'string', 'description': 'Genre'},
                        'date': {'type': 'number', 'description': 'Song release year'}
                    },
                    'required': ['file', 'title', 'artist', 'album' , 'genre', 'date']
                }
            }
        }
    }
)

tool = types.Tool(function_declarations=[getSongsDetails])
search_tool = types.Tool(google_search=types.GoogleSearch())

sys_instr = ("You are a music metadata expert. For every filename provided, "
                 "research the song to find its official title, artist, genre, album and release year(date) "
                 "Do not skip any files.")




@retry(
    stop=stop_after_attempt(10), # Increase attempts if the service is very busy
    wait=wait_exponential(multiplier=2, min=4, max=60), # Wait longer between tries
    retry=retry_if_exception_type(errors.ServerError), # Target the correct error
    reraise=True # Ensures the final failure still raises so you can catch it in the loop
)

def aiQuery(contents, **config_options):
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=contents,
            config=types.GenerateContentConfig(**config_options),
        )
        client.close()
        return response
    except exceptions.ServiceUnavailable as e:
        print(f"Server busy (503), retrying... {e}")
        raise e 
    
    except Exception as e:
        print(f"An error ocurred while acessing the api, returning changed data only...")
        raise e


def batchFetchData(musicList):
    
    filenames = [item['file'] for item in musicList]
    
    formatted_list = ", ".join(filenames)
    
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

    
    return response