import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

memory_file = "memory.json"

if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        memory = json.load(f)
else:
    memory = {
        "user_name": "Unknown",
        "mood_history": [],
        "conversation_history": []
    }

print("Therapist Bot: Hi there. How are you feeling today?")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Therapist Bot: Take care. I'm always here if you want to talk again.")
        break

    memory["conversation_history"].append({"user": user_input})

    if "i feel" in user_input.lower():
        feeling = user_input.lower().split("i feel")[-1].strip().split()[0]
        memory["mood_history"].append(feeling)

    if "my name is" in user_input.lower():
        name = user_input.lower().split("my name is")[-1].strip().split()[0]
        memory["user_name"] = name.capitalize()

    messages = [
        {"role": "system", "content": "You are a compassionate and thoughtful AI therapist. Respond with empathy, ask reflective questions, and help the user process their feelings."}
    ]

    for exchange in memory["conversation_history"][-6:]:
        if "user" in exchange:
            messages.append({"role": "user", "content": exchange["user"]})
        if "bot" in exchange:
            messages.append({"role": "assistant", "content": exchange["bot"]})

    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        bot_reply = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        bot_reply = "Sorry, something went wrong. Try again later."
        print(f"[Error]: {e}")

    print(f"Therapist Bot: {bot_reply}")
    memory["conversation_history"].append({"bot": bot_reply})

    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)
