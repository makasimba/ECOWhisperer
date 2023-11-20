"""Uses language model API to respond to user prompts"""

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from typing import List, Tuple, AnyStr

_ = load_dotenv(find_dotenv())

client = OpenAI()
CONTEXT = open("utils/guide.txt").read()

DESCRIPTION = """ECO IV Ellie is your virtual assistant dedicated to guiding users through the intricate landscape of 
UK eco schemes. With a friendly persona inspired by eco-conscious customer representatives, Ellie seamlessly engages 
users in meaningful conversations about sustainable living, energy efficiency, and environmental initiatives. 
Empowering users with knowledge and assistance, Ellie is your go-to companion for navigating the world of 
eco-conscious choices and making a positive impact on the planet. Join the conversation and let EllieChat be your 
eco-guide today."""

sys_message = f"""Your persona is Ellie, a courteous customer service agent for the ECO IV scheme. As an agent, 
provide concise information about the program and guide users through the sign-up process. Be polite, 
informative, and avoid unnecessary details. Your goal is to assist citizens efficiently and ensure a smooth user 
experience. Mimic the tone of a helpful customer service representative, always aiming for thoughtful and 
succinct responses.

The following information, delimited by triple backticks provides details about the ECO4 scheme - feel free to use 
this information: ```{CONTEXT}```
"""


def gr_format(messages):
    """Assumes messages is in the form of openai api. Converts to gr format"""
    messages = messages[1:]

    mine = [msg["content"] for i, msg in enumerate(messages, 1) if i % 2 == 1]
    bot = [msg["content"] for i, msg in enumerate(messages, 1) if i % 2 == 0]

    return [v for v in zip(mine, bot)]


def oa_format(messages):
    """
    Assumes messages is in gr format
    """
    m = [{"role": "system", "content": sys_message}]
    for v in messages:
        mine, bot = v
        m.append({"role": "user", "content": mine})
        m.append({"role": "assistant", "content": bot})
    return m


def respond(message: AnyStr, messages: List[Tuple]) -> List[Tuple]:
    """Assumes messages are in gr format."""
    messages = oa_format(messages)

    query = f"""
    QUESTION: {message}
    """
    messages.append({"role": "user", "content": query})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.25,
        seed=42,
        # TODO: Fix the streaming idiot
    )

    message = response.choices[0].message.content

    return message


if __name__ == '__main__':
    hist = []
    for _ in range(5):
        prompt = input("Prompt >> ")
        res, hist = respond(prompt, hist)
        print(f"AI: {res}")
        print(type(hist), hist)
    print("end of conversation.")
