from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import time, random

_ = load_dotenv(find_dotenv())

client = OpenAI()
CONTEXT = open("utils/guide.txt").read()
DESCRIPTION = """
Ellie is a helpful UK ECO IV scheme autonomous agent. Ellie will politely answer questions
about the scheme, check your eligibility and help you through the entire sign up, 
installation and post-installation stages
"""


def respond(prompt="Hi Ellie.", history=None):
    query = f"""
    Use the information delimited by triple backticks to answer the following question:

    INFORMATION: ```{CONTEXT}```
    QUESTION: {prompt}
    """

    sys_message = """Your persona is Ellie, a courteous customer service agent for the ECO IV scheme. As an
    agent, your role is to assist citizens by providing concise information about the program and guiding
    them through the sign-up process. Your approach is polite and informative. You engage users by posing pertinent 
    questions to determine their eligibility for the scheme, ensuring a seamless and user-friendly experience.
    
    Mimic the tone and style of a helpful customer service representative. And please remember to be thoughtful and 
    extremely concise in your responses. This is very important."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": sys_message},
            {"role": "user", "content": query}
        ],
        temperature=0.25,
        seed=42,
        max_tokens=50,
        # TODO: Fix the streaming idiot
    )
    message = response.choices[0].message.content
    # for i in range(len(message)):
    #     time.sleep(0.05)
    #     yield "" + message[: i + 1]
    return message


if __name__ == '__main__':
    print(respond("Tell me about this scheme of yours."))
