from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
   return render_template("home.html")




@app.route("/chat")
def chat():
   return render_template("chat.html")


@app.route("/api/chat", methods=["POST"])
def api_chat():
   """A minimal mock AI endpoint that returns a JSON reply.

   This is intentionally simple and local-only. Replace with a real AI
   service integration when ready (use environment variables for keys).
   """
   data = request.get_json(silent=True) or {}
   message = (data.get("message") or "").strip()

   if not message:
      reply = "Please send a message."
   elif "backache" in message.lower() or "backache" in message.lower():
      reply = "Backache solution test message"
   else:
      reply = f"AI (demo): I received your message: \"{message}\".\nThis is a mock response for development."

   return jsonify({"reply": reply})
if __name__ == "__main__":
    app.run(debug=True)
