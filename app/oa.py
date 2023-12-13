"""Uses A language model As An Autonomous ECO IV Agent"""
from typing import List, Tuple, AnyStr
from tools import get_date
from exceptions import MisuseException
from utils import oa_format

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from augment import augment

_ = load_dotenv(find_dotenv())

client = OpenAI()

INFO = open("/Users/makasimba/PycharmProjects/bot/docs/info.txt").read()
DELIMITER = "####"

# TODO: DEFINITELY NEED TO ITERATE ON THIS PROMPT AN IMBUE MORE HELPFUL AGENT LIKE CHARACTER THROUGH CoT
sys_message = f"""
Today is {get_date()}

Your persona is Ellie, a courteous customer service agent for the ECO4 scheme. As an agent, you provide concise
information about the scheme in no more than 3 short sentences, and guide users through the sign-up process.

Please keep our conversation polite, and concise. Avoid unnecessary details. Mimic the friendly and approachable
 tone of a helpful customer service representative.

Use the helpful information enclosed within {DELIMITER} for your responses:
    {DELIMITER}\n{INFO}\n{DELIMITER}

When the user asks to sign up, provide the link below in nicely formatted text, the link directs them to an ECO4 scheme
application form that they can fill in and submit:
    https://lpsuy8wre8p.typeform.com/to/kFOUvXH6

Think step by step, and remember to be thoughtful and succinct in your responses.
"""


def respond(message, messages):
    """Respond To User Queries."""
    # TODO: ADD AUGMENTATION HERE
    messages = oa_format(messages, sys_message)

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.42,
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
    return response


if __name__ == '__main__':
    # FOR DEBUGGING PURPOSES ONLY
    hist = []
    for _ in range(5):
        prompt = input("Prompt >> ")
        res = respond(prompt, hist)

        print(f"AI: {res}")
    print("<EOF>")
