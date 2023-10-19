import assemblyai as aai
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())


def speech_to_text(audio_file):
    aai.settings.api_key = os.getenv("AS_API_KEY")
    print(1)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    print(2)
    print(transcript.text)

a = 'recorded_.mp3'
print(speech_to_text(a))