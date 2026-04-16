# 🚀 AI Event Assistant

An intelligent event reminder system that delivers **personalized notifications and gift suggestions** using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Telegram automation.

Unlike traditional reminder apps, this system understands user preferences and generates **context-aware, thoughtful messages**.

---

## 📌 Features

* 📅 Automated event reminders (birthdays, special occasions)
* 🧠 Personalized suggestions using RAG-based memory
* 🤖 AI-generated reminder messages and gift ideas
* 📩 Telegram bot integration for real-time alerts
* 🔐 Secure handling of API keys using `.env`
* ⚙️ Daily automated scheduler

---

## 🛠️ Tech Stack

* **Language:** Python
* **LLM:** Ollama (local models like Llama3)
* **Vector DB:** ChromaDB
* **Automation:** Telegram Bot API
* **Data Handling:** Pandas
* **Environment Management:** python-dotenv

---

## 🧩 Project Structure

```
ai-event-assistant/
│
├── data/
│   └── events.csv          # Event data (names, dates, notes)
│
├── db/                     # Vector database (RAG memory)
│
├── src/
│   ├── main.py             # Entry point
│   ├── notifier.py         # Telegram message sender
│   ├── parser.py           # Event processing
│   ├── rag.py              # Memory retrieval (ChromaDB)
│   ├── scheduler.py        # Daily automation
│   ├── llm.py              # LLM interaction
│   └── setup_memory.py     # Initial memory setup
│
├── .env                    # Environment variables (NOT pushed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-event-assistant.git
cd ai-event-assistant
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup Environment Variables

Create a `.env` file in the root directory:

```
TELEGRAM_TOKEN=your_bot_token
CHAT_ID=your_chat_id
```

---

### 4. Run the Project

```bash
python src/main.py
```

---

### 5. (Optional) Run Scheduler

```bash
python src/scheduler.py
```

---

## 🧠 How It Works

1. Event data is stored in a CSV file
2. User preferences are stored in a vector database (ChromaDB)
3. RAG retrieves relevant context for each person
4. LLM generates:

   * Personalized reminder messages
   * Gift suggestions
5. System sends notification via Telegram

---

## 🎯 Use Cases

* Smart personal reminder assistant
* AI-powered notification systems
* Productivity automation tools
* Personalized gifting assistant

---

## 🔐 Security

* Sensitive data is stored in `.env`
* `.env` is excluded using `.gitignore`
* No API keys are exposed in the repository

---

## 🚀 Future Improvements

* Web dashboard (React + Flask)
* WhatsApp / Email integration
* Automatic contact sync
* Advanced preference learning system

---

## 👨‍💻 Author

**Adhil**
Final Year Computer Science Student

---

## ⭐ Acknowledgements

* Open-source LLM ecosystem
* Telegram Bot API
* ChromaDB for vector storage

---

## 📄 License

This project is open-source and available under the MIT License.
