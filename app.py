from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

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
def chat():
    return render_template("chat.html")


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        reply = "Please send a message."
    elif "backache" in message.lower():
        reply = "Backache solution test message"
    else:
        reply = f"AI (demo): I received your message: \"{message}\".\nThis is a mock response for development."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
