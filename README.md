# pure-python-echo-agent
Pure Python Echo Agent is a lightweight, framework-free AI chatbot that uses the OpenAI Chat API to respond to user input in real time. Designed as a starting point for anyone interested in building AI agents with plain Python, this project includes a simple event loop, a system prompt, and real-time interaction via the terminal. Ideal for beginners, educators, and developers who want to understand LLM-based agents from the ground up—without the overhead of LangChain or other libraries.

## 🚀 What It Does

This Echo Agent:
- Accepts user input from the terminal
- Sends it to OpenAI’s ChatCompletion API
- Echoes the model's response back to the user
- Remembers the conversation within the session

It's the perfect starting point for learning how AI agents work—without the complexity of LangChain, CrewAI, or AutoGen.

## 🗂️ Project Structure

pure-python-echo-agent/
├── main.py # Core agent loop
├── config.py # API key management
├── requirements.txt
└── README.md

## 🛠️ Requirements

- Python 3.8+
- An OpenAI API key

Install dependencies:

```bash
pip install -r requirements.txt
