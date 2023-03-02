import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import openai
from utils import *

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def openai_chatgpt(prompt: str):
    """
    This function allows to make api call to OpenAI.

    Args:
        prompt (str): The prompt passed to the OpenAI API.

    Returns:
        response (str): The response from OpenAI.
    """
    completion = openai.ChatCompletion.create(
        model=MODEL,  # Model to use.
        temperature=TEMPERATURE,  # This parameter controls variability of the response.
        messages=[
            {
                "role": ROLE,  # whether we will act as user or assistant.
                "content": prompt,
            }
        ],
    )
    # The above parameters is to be changed as per the business needs.
    return completion["choices"][0]["message"]["content"]


# if __name__ == "__main__":
#     print(openai_chatgpt("Complete the sentence for me: My name is Monkey D. Luffy. I will be..."))
# print(os.getenv("OPENAI_API_KEY"))
