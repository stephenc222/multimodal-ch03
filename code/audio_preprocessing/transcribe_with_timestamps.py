import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def transcribe_with_timestamps(audio_path):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    with open(audio_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1",
            response_format="verbose_json",
            timestamp_granularities=["word"]
        )
    return transcription.words

if __name__ == "__main__":
    # Using the same video mp4 file as the example for video processing
    path = "data/video/sample_video/customer_support_demo.mp4"
    words = transcribe_with_timestamps(path)
    for word in words:
        print(f"Start: {word.start:.2f}s, End: {word.end:.2f}s, Text: {word.word}")