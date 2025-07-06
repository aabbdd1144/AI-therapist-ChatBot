# 🧠 GPT-Powered Therapist Chatbot

This is a conversational mental health chatbot powered by **OpenAI’s ChatGPT (gpt-3.5-turbo)**. It simulates an empathetic AI therapist that can remember your past conversations, track emotional cues, and support reflective dialogue in a safe, private environment.

---

## ✨ Features

- 🤖 Built with OpenAI’s GPT-3.5 (Chat API)
- 💬 Maintains full chat history for contextual replies
- 😔 Tracks moods based on phrases like “I feel…”
- 🧠 Stores memory in a local `memory.json` file
- 🔐 Keeps your OpenAI key safe via `.env`

---

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/yourusername/therapist-chatbot-gpt.git
cd therapist-chatbot-gpt 
```

### 2. Install Dependencies
 ```  
pip install -r requirements.txt
```
### 3. Create a .env File
```
OPENAI_API_KEY=your_openai_api_key_here
```
You can get your API key from https://platform.openai.com/account/api-keys

###  4. Run the Chatbot
```
python chatbot.py
```
### 🛑 Exit the Chat
Type any of the following to quit:

```
exit
quit
bye
```
### 📦 File Structure
├── chatbot.py            Main script
├── memory.json           Chat + mood memory (auto-generated)
├── .env                  API key (not uploaded)
├── .gitignore            Ignores secrets and cache
├── requirements.txt      Dependencies
└── README.md            -> You’re here

### 🔐 Important
Your API key is not shared if you use .env and .gitignore properly.

This chatbot runs locally only — no data is sent anywhere besides OpenAI.

### 🧠 Ideas for Future Upgrades
GUI with Tkinter or Streamlit

Sentiment analysis / emotional graphs

Voice input & output

Topic extraction & journaling

Hugging Face or web deployment

### 📄 License
This project is free to use for personal, educational, and research purposes. Attribution appreciated.

