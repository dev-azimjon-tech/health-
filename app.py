from flask import Flask, render_template, request, jsonify
import os
import json
from dotenv import load_dotenv
import openai  #type:ignore
from difflib import get_close_matches

load_dotenv()

app = Flask(__name__)


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY #type:ignore

DRUGS_FILE = "drugs.json"

def load_drugs():
    try:
        if os.path.exists(DRUGS_FILE):
            with open(DRUGS_FILE, "r", encoding="utf-8") as f:
                content = f.read()
                if not content.strip():
                    return []
                return json.load(f)
        return []
    except json.JSONDecodeError:
        print("Error: drugs.json file is corrupted")
        return []
    except Exception as e:
        print(f"Error loading drugs file: {e}")
        return []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/drugs", methods=["GET"])
def drugs():
    query = request.args.get("query", "").strip()
    all_drugs = load_drugs()

    result = None
    if query:
        drug_names = [d["name"] for d in all_drugs]
        matches = get_close_matches(query, drug_names, n=1, cutoff=0.6)
        
        if matches:
            best_match = matches[0]
            for d in all_drugs:
                if d["name"] == best_match:
                    result = d
                    break

    return render_template("drugs.html", drug=result)

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@app.route("/api/chat", methods=["POST"])
def chat_api():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.json
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON format"}), 400
    
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Please write a message"}), 400
    
    if len(user_message) > 1000:
        return jsonify({"error": "Message too long. Please limit to 1000 characters"}), 400

    try:
        response = openai.ChatCompletion.create( #type:ignore
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

@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
