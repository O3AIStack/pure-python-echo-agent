# This is part of the Pure Python AI Agent Series — a content and code initiative to help developers build useful LLM agents without depending on frameworks.
# May 31, 2025
# O3AIStack.com
# Version 1.0
# main.py

import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

# Load API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

# Define the system prompt
system_prompt: ChatCompletionMessageParam = {
    "role": "system",
    "content": "You are a helpful assistant. Echo the user's input clearly and helpfully."
}

# Initialize memory
conversation: list[ChatCompletionMessageParam] = [system_prompt]

print("🤖 Echo Agent is running. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in {"exit", "quit"}:
        print("Agent: Goodbye!")
        break

    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        reply = response.choices[0].message.content
        print("Agent:", reply)

        conversation.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("Agent Error:", str(e))
