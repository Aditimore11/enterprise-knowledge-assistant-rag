chat_history = []

def add_message(role, message):
    chat_history.append({
        "role": role,
        "message": message
    })

def get_history():

    history = ""

    for item in chat_history:
        history += f"{item['role']}: {item['message']}\n"

    return history