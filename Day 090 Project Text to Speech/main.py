import os
from google.cloud import texttospeech
import PyPDF2


# Generate text empty variable
text = ""

# Specify File path
FILE_PATH = './Rafael não sabe ler-converted.pdf'

# Open .pdf file
with open(FILE_PATH, mode='rb') as f:
    # Create pdf object
    reader = PyPDF2.PdfFileReader(f)
    # loop through pages
    for page in reader.pages:
        # Add text extracted in each page
        text += page.extractText()

# Must specify file path containing json with APIKEY for GOOGLE CLOUD API
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Call text to speech API Client
client = texttospeech.TextToSpeechClient()

# Create input text for API based on text variable
input_text = texttospeech.SynthesisInput(text=text)

# Define voice
voice = texttospeech.VoiceSelectionParams(
    language_code="pt-BR",
    name="pt-BR-Standard-A",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
)

# Define audio encoding type
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Request to synthesize speech
response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
