import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from src import gradio_helper_chatbot, gradio_interface

demo = gradio_interface(gradio_helper_chatbot)
# Use this config when running on Docker
demo.launch(server_name="0.0.0.0", server_port=7000)
# To run on local machine
# demo.launch()