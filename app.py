import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# OpenRouter API (free for light use)
OPENROUTER_API_KEY = "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"  # Get one at https://openrouter.ai/

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/diagnosis')
def diagnosis():
    return render_template('diagnosis.html')

@app.route('/ibn_sina')
def ibn_sina():
    return render_template('ibn_sina.html')

@app.route('/workflow')
def workflow():
    return render_template('workflow.html')

@app.route('/mental_health')
def mental_health():
    return render_template('mental_health.html')

@app.route('/rural_care')
def rural_care():
    return render_template('rural_care.html')

@app.route('/chat_ai', methods=['GET', 'POST'])
def chat_ai():
    if request.method == 'POST':
        user_message = request.json.get('message', '')

        # Call OpenRouter API (Mistral 7B Instruct)
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": user_message}
            ],
            "max_tokens": 100
        }
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=20
            )
            if response.status_code == 200:
                data = response.json()
                ai_reply = data['choices'][0]['message']['content']
            else:
                ai_reply = "Sorry, the AI service is currently unavailable."
        except Exception as e:
            ai_reply = "Error contacting the AI service."

        return jsonify({'reply': ai_reply})

    return render_template('chat_ai.html')

if __name__ == '__main__':
    app.run(debug=True)
