import gradio as gr
from oa import respond, foo
from frontend import Seafoam
from frontend import EMERALD


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
    description="",
    examples=[
        "How Can I Check My Eligibility for the ECO 4 Scheme?",
        "How Can I Apply for the Eco IV Scheme?",
        "Explain The ECO4 Scheme To Me Like I Am 10.",
        "Will I Really Get a Free Boiler? What's The Catch",
        "What are Some of The Benefits of ECO4?",
        "What's The Timeline for Implementation of Approved Eco 4 Improvements?",
        "What Types of Improvements Does the Eco 4 Scheme Cover?",
    ],
    css="footer {visibility: hidden}"
)

if __name__ == "__main__":
    demo.queue().launch()
