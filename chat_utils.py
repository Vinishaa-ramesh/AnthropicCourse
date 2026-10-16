
from dotenv import load_dotenv
from groq import Groq
import os

def init_model(model_name: str):
    load_dotenv()
    global client, model
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    model = model_name

# Add messages to conversation history
def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

# Stream the response from Groq
def chat(messages, system=None, temperature=1.0):
    if system:
        messages = [
            {"role": "system", "content": system}
        ] + messages

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=1000,
        temperature=temperature,
        stream=True
    )

    full_response = ""

    for chunk in response:
        content = chunk.choices[0].delta.content

        if content:
            print(content, end="", flush=True)
            full_response += content

    print()
    return full_response