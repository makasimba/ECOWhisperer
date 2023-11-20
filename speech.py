"""
Implementation of the speech component for the bot.
"""
from openai import OpenAI
import playsound

audio_client = OpenAI()

s = """Sure! I'd be happy to tell you about our scheme. The ECO4 scheme is a government initiative aimed at helping 
households in the UK reduce their energy bills and carbon emissions. It provides funding for energy efficiency 
improvements such as insulation, heating upgrades, and renewable technologies. By participating in the scheme, 
you can make your home more energy-efficient and environmentally friendly.
"""


def speak(script=s):
    response = audio_client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=s,
    )
    response.stream_to_file("output.mp3")
    playsound.playsound("output.mp3")


def speech_stream(script=s):
    response = audio_client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=script,
    )
    response.stream_to_file("output.mp3")
    playsound.playsound("output.mp3")


if __name__ == "__main__":
    speak.stream_to_file("output.mp3")
    playsound.playsound("output.mp3")
