# Setup Details

## Create the environment
python -m venv azureoai_env

## Activate the environment (Windows)
azureoai_env\Scripts\activate

## Install dependencies
pip install -r requirements.txt

# Important Note
These new transcribe models leverage the Speech to Text API not the RealTime API, which uses WebSockets.  The documentation for the API can be found on the OpenAI site.

[Speach to Text API](https://platform.openai.com/docs/guides/speech-to-text)