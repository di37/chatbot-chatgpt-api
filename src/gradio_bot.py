import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from src.chatgpt_api import openai_chatgpt
import gradio as gr


def gradio_helper_chatbot(input: str, history=[]):
    """
    Function that is used for connecting the chatbot interface, user input and the response that will be received from OpenAI.

    Args:
        input (str): user input
        history (list): history of user input and responses from OpenAI API. It represents the state.

    Returns:
        history, history (list, list): It is in this way that gradio demos will take in update as end of the function is reached.
    """
    # Combining current and previous conversation both input and response. 
    s = list(sum(history, ()))
    s.append(input)
    inp = " ".join(s)
    # Output result from OpenAI API
    output = openai_chatgpt(inp)
    # This will allow to save the previous chat and allow to continue the conversation
    # with the chatbot
    history.append((input, output))
    return history, history


def gradio_interface(helper_function):
    """
    This function allows implementation of fully functional chatbot interface.

    Args:
        helper_function (function): This is helper function to be passed to gradio demo.
    """
    with gr.Blocks() as demo:
        gr.Markdown("""
            <h1><center>Chatbot with ChatGPT API & Gradio</center></h1>
        """)
        chatbot = gr.Chatbot()
        state = gr.State([])

        with gr.Row():
            txt = gr.Textbox(
                show_label=False, placeholder="Enter Text and Press Enter."
            ).style(container=False)

        txt.submit(helper_function, [txt, state], [chatbot, state])

    return demo
