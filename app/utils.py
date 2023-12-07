

tools = []

def oa_format(messages, system_message):
    """
    Assumes messages is in Gradio format. Converts messages to OAI format.
    """
    m = [{"role": "system", "content": system_message}]
    for v in messages:
        mine, bot = v
        m.append({"role": "user", "content": mine})
        m.append({"role": "assistant", "content": bot})
    return m


def evaluate(user_query):
    """Assesses the user input for misuse."""
    user_query = user_query.replace(DELIMITER, "")
    response = client.moderations.create(
        input=user_query,
    )
    if response.results[0]['flagged']:
        raise MisuseException

