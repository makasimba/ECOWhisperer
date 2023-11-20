import gradio as gr
from oa import respond
from frontend import Seafoam
import time


demo = gr.ChatInterface(  # TODO: Remove the "Chatbot" text in the top left corner
    fn=respond,
    chatbot=gr.Chatbot(container=False, avatar_images=(None, None), layout="bubble"),
    retry_btn=None,
    stop_btn=None,
    undo_btn=None,
    clear_btn=None,
    theme=Seafoam(),
    title="ECO IV ELLIE",  # TODO: change the text color from black to emerald and make the font size bigger
    description="",
    examples=[
        "What's The Catch?",
        "How Can I Check My Eligibility for the ECO 4 Scheme?",
        "How Can I Apply for the Eco 4 Scheme?",
        "Explain The ECO4 Scheme To Me Like I Am 10.",
        "Why is The UK Government Doing This?",
        "Will I really get a free boiler?",
        "What are The Benefits of ECO4?",
        "What Is The Timeline for Implementation of Approved Eco 4 Improvements?",
        "What Types of Energy Efficiency Improvements Does the Eco 4 Scheme Cover?",
    ],  # TODO: Change the text color to emerald or something.
    css="footer {visibility: hidden}"
)

if __name__ == "__main__":
    demo.queue().launch()
