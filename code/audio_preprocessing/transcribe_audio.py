import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def transcribe_audio(audio_path):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    with open(audio_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    return transcription.text

if __name__ == "__main__":
    # Using the same video mp4 file as the example for video processing
    EXAMPLE_FILE_PATH = "data/video/sample_video/customer_support_demo.mp4"
    text = transcribe_audio(EXAMPLE_FILE_PATH)
    print("Whisper Transcription:", text)