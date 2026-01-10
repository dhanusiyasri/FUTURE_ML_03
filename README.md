# 🤖 Customer Support Chatbot

A chatbot application built using **Streamlit** and **Dialogflow** that helps users resolve common customer support issues such as login problems, refunds, delivery delays, and complaints.  
The chatbot uses **Dialogflow’s built-in Machine Learning (NLP)** to understand user queries and respond appropriately.

---

## 📌 Project Overview

Customer support teams often handle repetitive queries.  
This project demonstrates how a **chatbot interface** can automate customer support using **Natural Language Processing (NLP)**.

The chatbot:
- Accepts user input in natural language
- Identifies the intent (login issue, refund, delivery, complaint, etc.)
- Responds with relevant support information
- Provides a clean, chat-style UI similar to modern chat applications

---

## 🧠 How It Works

User
->
Streamlit Chat UI
->
Dialogflow (ML-based Intent Detection)
->
Bot Response


- **Streamlit**: Frontend chat interface  
- **Dialogflow**: NLP + Machine Learning for intent detection  
- **Google Cloud Service Account**: Secure authentication  

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Dialogflow (Google Cloud)
- Google Auth (Service Account)
- REST APIs

---

## 🎯 Features

- Chat-style user interface
- Supports multiple customer issues:
  - Login problems
  - Refund requests
  - Delivery delays
  - Complaints
  - General support queries
- Session-based chat history
- Easy to deploy on Streamlit Cloud
- Beginner-friendly and internship-ready


---

## 📂 Project Structure
``` bash
├── streamlit_app.py # Chatbot UI
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignored files (secrets, cache)
```

---

## ⚠️ Important Notes

- `service_account.json` is **NOT uploaded** to GitHub for security reasons.
- Google credentials are managed using **Streamlit Secrets** during deployment.
- No backend server deployment is required (Dialogflow handles ML internally).

---

## 🚀 How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Add Google Service Account

- Create a service account in Google Cloud
- Enable Dialogflow API
- Download the JSON key
- Place it locally (do NOT upload to GitHub)

### 3️⃣ Run Streamlit app

```bash
streamlit run streamlit_app.py
```

### 🌍 Deployment (Streamlit Cloud)

1. Push project to GitHub (excluding secrets)
2. Go to https://share.streamlit.io
3. Select your repository and streamlit_app.py
4. Add Google service account JSON in Streamlit Secrets
5. Deploy 🎉

### 🧪 Sample Queries

- i can't login
- i want refund
- my delivery is late
- bad service
- help

### 🔮 Future Enhancements

- Add database logging for conversations
- Support multiple languages
- Integrate with WhatsApp / Telegram
- Add sentiment analysis
- Connect to real customer support systems

### This project is for educational and internship purposes.
