from exceptions import MisuseException

tools = []


def oa_format(messages, system_message):
    """
    Assumes messages is in Gradio format - list of tuples.
    Converts messages to OAI format - list of dictionaries.
    """
    m = [
        {"role": "system", "content": system_message},
        {"role": "assistant", "content": "Hello! I'm Ellie, your friendly neighbourhood ECO4 guide."},
    ]

    for v in messages:
        mine, bot = v
        if mine is None:
            m.append({"role": "user", "content": ""})
            m.append({"role": "assistant", "content": bot})
        else:
            m.append({"role": "user", "content": mine})
            m.append({"role": "assistant", "content": bot})
    return m


def foo(message, messages):
    """For debugging purposes only."""
    return "..."
