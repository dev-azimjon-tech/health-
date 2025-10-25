from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DRUGS_FILE = "drugs.json"
#I will add the api key to .env file

API_KEY = os.getenv('AI_API_KEY')



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
def chat_route():
    return render_template("chat.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please provide a message."})

    try:
        response = genai.chat.create(
            model="chat-bison-001",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        ai_reply = response.last["content"] if response.last else "No response from AI."
        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
