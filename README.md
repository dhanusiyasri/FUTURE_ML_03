# 🤖 Customer Support Chatbot  
### Streamlit + Dialogflow + Flask (Machine Learning)

An end-to-end **Customer Support Chatbot** built using **Streamlit** for the user interface, **Dialogflow** for intent routing, and a **Flask-based Machine Learning backend** for intelligent response generation.

This project demonstrates how modern chatbots combine UI, NLP platforms, and custom ML models.

---

## 📌 Project Overview

Customer support teams often receive repetitive queries such as:
- Login issues
- Refund requests
- Delivery delays
- Complaints

This chatbot automates these interactions by:
- Accepting natural language input
- Routing queries through Dialogflow
- Using a trained ML model to classify user intent
- Returning meaningful responses through a chat-style interface

---

## 🧠 System Architecture


User
->
Streamlit Chat UI
->
Dialogflow (Intent Routing)
->
Flask Webhook (ML Model)
->
Response to User

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – Chatbot user interface
- **Dialogflow (Google Cloud)** – NLP & intent routing
- **Flask** – Webhook server
- **Scikit-learn** – Machine learning model
- **Pandas** – Data processing
- **Ngrok** – Local webhook exposure (for testing)

---

## 🎯 Features

- ChatGPT-like chat interface
- Handles multiple customer issues:
  - Login issues
  - Refund issues
  - Delivery issues
  - Complaints
  - General queries
- ML-based intent classification
- Modular and scalable architecture
- Beginner and internship friendly

---

## 📂 Project Structure


``` bash
│
├── streamlit_app.py # Streamlit chatbot UI
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files
│
├── model/
│ ├── train_model.py # ML training script
│ ├── intent_model.pkl # Trained ML model
│ └── vectorizer.pkl # TF-IDF vectorizer
│
└── webhook/
└── app.py # Flask webhook (ML backend)
```

---

## ⚠️ Security Notes

- `service_account.json` is **NOT uploaded to GitHub**
- Google credentials are stored locally or via environment variables
- Dataset files are excluded to keep the repository lightweight

---

## 🚀 How to Run Locally

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

```

### 2️⃣ Train the Machine Learning Model

```bash 
cd model
python train_model.py
```

Ensure the following files are generated:

```bash
Ensure the following files are generated:
```

### 3️⃣ Run Flask Webhook

```bash
cd webhook
python app.py
```

Expected output:

```bash
Running on http://127.0.0.1:5000
```

### 4️⃣ Expose Webhook (Local Testing)

```bash
ngrok http 5000
```

Copy the HTTPS URL and update Dialogflow → Fulfillment:

```bash

https://xxxx.ngrok-free.dev/webhook
```

### 5️⃣ Configure Dialogflow

- Create an intent: Customer_Support
- Add training phrases:

    - i can't login
    - i want refund
    - delivery is late
    - bad service
    - help

- Enable webhook fulfillment
- Remove static text responses

### 6️⃣ Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

Open in browser:

```bash
http://localhost:8501
```

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

---
## 📬 Acknowledgment
This project was completed as part of Future Interns – Machine Learning Task 3, focusing on practical implementation of chatbot.


---
### This project is for educational and internship purposes.
