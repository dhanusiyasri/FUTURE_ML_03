import pandas as pd
import re, pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
print("SCRIPT STARTED")
df = pd.read_csv("../data/twcs.csv")
df = df[df["inbound"] == True][["text"]].dropna()
print("DATA LOADED")
def label_intent(text):
    text = text.lower()

    if any(word in text for word in ["login", "sign in", "password"]):
        return "login_issue"

    elif any(word in text for word in ["refund", "money back", "returned"]):
        return "refund_issue"

    elif any(word in text for word in ["delivery", "delayed", "late", "not delivered", "order"]):
        return "delivery_issue"

    elif any(word in text for word in ["bad", "worst", "complaint", "disappointed", "not satisfied"]):
        return "complaint"

    else:
        return "general_query"

df["intent"] = df["text"].apply(label_intent)
print("INTENTS LABELED")
def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text.lower()

df["clean_text"] = df["text"].apply(clean_text)
print("TEXT CLEANED")
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["clean_text"])
y = df["intent"]
print("TEXT VECTORIZED")
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)
print("MODEL TRAINED")
pickle.dump(model, open("intent_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
print("MODEL AND VECTORIZER SAVED")