import gradio as gr
from oa import respond, foo
from frontend import Seafoam
from frontend import EMERALD


DESC = """ECO IV Ellie is your virtual assistant dedicated to guiding users through the intricate landscape of 
UK ECO schemes. A friendly persona inspired by eco-conscious customer representatives, Ellie seamlessly engages 
users in meaningful conversations about sustainable living, energy efficiency, and environmental initiatives. 
Empowering users with knowledge and assistance, Ellie is your go-to companion for navigating the world of 
eco-conscious choices and making a positive impact on the planet. Join the conversation and let Ellie be your 
eco-guide today."""

demo = gr.ChatInterface(
    fn=respond,
    chatbot=gr.Chatbot(
        bubble_full_width=False,
        container=False,
        avatar_images=(None, "./avatars/a11.jpeg"),
        layout="bubble"
    ),
    retry_btn=None,
    stop_btn=None,
    undo_btn=None,
    clear_btn=None,
    theme=Seafoam(),
    title=f'<h1 style="color: #009C68; font-size: 2rem; text-align: center; font-family: monospace;">ECO <strong '
          f'style="color: {EMERALD}">IV</strong> ELLIE</h1>',
    examples=[
        "How Do I Check Eligibility for the ECO 4 Scheme?",
        "How Do I Apply for the ECO IV Scheme?",
        "Explain The ECO4 Scheme To Me Like I Am 10.",
        "Will I Really Get a Free Boiler? What's The Catch",
        "What are Some of The Benefits of ECO4?",
        "What's The Timeline for Implementation of Approved Eco 4 Improvements?",
        "What Types of Improvements Does the Eco 4 Scheme Cover?",
    ],
    css="footer {visibility: hidden}",
    description="",
)

if __name__ == "__main__":
    demo.queue().launch()
