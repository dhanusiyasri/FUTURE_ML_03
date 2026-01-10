from flask import Flask, request, jsonify
import pickle, re

app = Flask(__name__)

model = pickle.load(open("../model/intent_model.pkl", "rb"))
vectorizer = pickle.load(open("../model/vectorizer.pkl", "rb"))

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text.lower()

@app.route("/webhook", methods=["POST"])
def webhook():
    user_text = request.json["queryResult"]["queryText"]
    vec = vectorizer.transform([clean_text(user_text)])
    intent = model.predict(vec)[0]

    responses = {
    "login_issue": "🔐 Please reset your password or contact support.",
    "refund_issue": "💰 Refunds are processed within 5–7 business days.",
    "delivery_issue": "📦 We’re checking your delivery status.",
    "complaint": "🙏 Sorry for the inconvenience. We’ll escalate this.",
    "general_query": "🤝 How can I help you? You can ask about login, refund, or delivery."
}
    
    return jsonify({"fulfillmentText": responses[intent]})

app.run(port=5000)
