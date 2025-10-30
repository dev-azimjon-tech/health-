from flask import Flask, render_template, request, jsonify
import os
import json
from dotenv import load_dotenv
import openai  # <-- OpenAI library

load_dotenv()

app = Flask(__name__)


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

DRUGS_FILE = "drugs.json"

def load_drugs():
    if os.path.exists(DRUGS_FILE):
        with open(DRUGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/drugs", methods=["GET"])
def drugs():
    query = request.args.get("query", "").strip().lower()
    all_drugs = load_drugs()

    result = None
    if query:
        for d in all_drugs:
            if d["name"].lower() == query:
                result = d
                break

    return render_template("drugs.html", drug=result)

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.json
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please write a message."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        reply_text = response.choices[0].message.content
        return jsonify({"reply": reply_text})
    except Exception as e:
        return jsonify({"reply": f"Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
