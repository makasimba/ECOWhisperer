import gradio as gr
from app.oa import respond
from app.frontend import Seafoam
from app.frontend import EMERALD

demo = gr.ChatInterface(
    fn=respond,

    chatbot=gr.Chatbot(
        value=[(None, "Hi 👋. I'm Ellie 😇, your friendly neighbourhood ECO4 scheme whisperer.")],
        bubble_full_width=False,
        container=False,
        avatar_images=(None, "./avatars/a11.jpeg"),
        layout="bubble",
    ),

    retry_btn=None,
    stop_btn=None,
    undo_btn=None,
    clear_btn=None,
    theme=Seafoam(),
    title=f'<h1 style="color: #009C68; font-size: 2rem; text-align: center; font-family: monospace;">ECO <strong '
          f'style="color: {EMERALD}">IV</strong> ELLIE</h1>',
    examples=[
        "How Do I Apply for the ECO IV Scheme?",
        "Explain The ECO4 Scheme To Me Like I Am 10.",
        "Will I Really Get a Free Boiler? What's The Catch",
        "What Types of Improvements Does the Eco 4 Scheme Cover?",
    ],
    css="footer {visibility: show}",
    description="",
)


def main():
    demo.queue().launch()


if __name__ == "__main__":
    main()
