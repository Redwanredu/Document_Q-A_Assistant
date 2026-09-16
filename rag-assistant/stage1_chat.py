import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

history = []  # list of dicts: {"role": "user"/"assistant", "content": "..."}

print("Chat started. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=history,
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})

    print(f"\nBot: {reply}\n")