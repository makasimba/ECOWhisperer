"""
Implementation of the speech component for the bot.
"""
from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="fable",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")