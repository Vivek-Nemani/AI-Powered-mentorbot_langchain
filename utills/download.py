def generate_chat_text(chat_log):
    text = ""
    for role, message in chat_log:
        text += f"{role.upper()}:\n{message}\n\n"
    return text
