


# Project Summary
This project was built with the intent of enriching the data for your audio files like .mp3, .wav or .flac
it uses the gemini api to query for data of the audio based in its filename and fetches the data in a structured model.
it queries the data by batches to save on api request.
the app itself is built on a fragile structure and heavely relies on the ai, which can alucinate and return wrong or unprecise data.
the app allows for the user to select which tags to modify and which files to exclude from the modification.

# How to run de application


## step 1:
    run git clone to get the repository on your system
    '''bash
    git clone https://github.com/Mauricio-Sch-prog/get_music_data-python.git
    '''

    or either download the repository folder

## step 2:
    if you don't yet have uv(Astral) on your system, run:
    macOS/Linux: ' -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh'
    Windows (PowerShell): 'powershell -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"'

## step 3:
    run the app on your terminal with 'uv run main.py'