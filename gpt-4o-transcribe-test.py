import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the Azure OpenAI client with values from .env
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Open the audio file
audio_file = open("audio_hello_world.wav", "rb")

# Create the transcription
transcription = client.audio.transcriptions.create(
    model=os.getenv("AZURE_OPENAI_MODEL"),  # Get model name from .env
    file=audio_file
)

# Print the transcription text
print(transcription.text)