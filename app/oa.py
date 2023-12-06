"""Uses A language model As An Autonomous ECO IV Representative"""

import random
import time
from typing import List, Tuple, AnyStr
import threading, multiprocessing
from tools import get_date

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from augment import augment

from speech import speech_stream

_ = load_dotenv(find_dotenv())

client = OpenAI()
CONTEXT = open("/Users/makasimba/PycharmProjects/bot/docs/guide.txt").read()

# TODO: DEFINITELY NEED TO ITERATE ON THIS PROMPT AN IMBUE MORE HELPFUL AGENT LIKE CHARACTER THROUGH CoT
sys_message = f"""
Your persona is Ellie, a courteous customer service agent for the ECO IV scheme. As an agent, 
provide concise information about the program and guide users through the sign-up process.

Be polite, informative, and avoid unnecessary details. Your goal is to assist citizens efficiently
and ensure a smooth user experience.

Mimic the tone of a helpful customer service representative, always aiming for thoughtful and 
succinct responses.

Use three sentences at most in your response and keep your answers as concise as possible.
"""


def oa_format(messages, system_message):
    """
    Assumes messages is in Gradio format. Converts messages to OAI format.
    """
    m = [{"role": "system", "content": system_message}]
    for v in messages:
        mine, bot = v
        m.append({"role": "user", "content": mine})
        m.append({"role": "assistant", "content": bot})
    return m


tools = [
]


def respond(message: AnyStr, messages: List[Tuple]) -> List[Tuple]:
    """Respond To User Queries."""
    # TODO: ADD AUGMENTATION HERE

    messages = oa_format(messages, sys_message)
    context = CONTEXT
    query = f"""Use the following piece of information to respond the user message at the end:\nToday is {get_date()}\n\n{context}\n\n{message}"""

    messages.append({"role": "user", "content": query})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        seed=42,
        stream=True,
    )

    completion = ""
    for chunk in response:
        try:
            completion += chunk.choices[0].delta.content
            yield completion
        except TypeError:
            break
        finally:
            # TODO: DYNAMIC REAL-TIME TEXT-TO-SPEECH STREAMING
            ...

    return response


def foo(message, messages):
    """For debugging purposes only."""
    return "..."


if __name__ == '__main__':
    # FOR DEBUGGING PURPOSES ONLY
    hist = []
    for _ in range(5):
        prompt = input("Prompt >> ")
        res = respond(prompt, hist)

        print(f"AI: {res}")
    print("<EOF>")
