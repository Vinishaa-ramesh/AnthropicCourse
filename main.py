from chat_utils import init_model, add_user_message, add_assistant_message, chat

# Load API key
model_name = "openai/gpt-oss-120b"
init_model(model_name)

# Chatbot simulation
messages = []

while True:
    user_input = input("> ")

    if user_input.lower() in ["quit", "exit"]:
        break

    add_user_message(messages, user_input)

    answer = chat(messages)
    print(answer)

    add_assistant_message(messages, answer)