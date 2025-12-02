🩺 Health — AI Symptom Checker (Prototype)

Health is a small web application for checking symptoms using an AI-backed symptom checker.
It provides a clean and minimal interface where users can describe their symptoms and receive preliminary AI-based feedback.
This project is a prototype/demo and not a substitute for professional medical advice.

🚀 Key Features

No registration required — users can check symptoms without creating an account.

AI symptom checker — integration point for a medical LLM or external API (e.g., Gemini).

Drug search (coming soon) — placeholder for drug lookup and related information.

Minimal, mobile-friendly UI — built with Flask and Tailwind CSS.

Optional premium model support — conceptual support for optimized AI models.

🧠 AI Chat Demo

A minimal AI Chat demo is available at the /chat route.
It currently uses a mock local endpoint (/api/chat), which you can later replace with a real AI service.

⚠️ Disclaimer

This repository is intended for educational and demonstration purposes only.
Do not rely on it for real medical diagnosis or treatment.

🧩 Developer Setup

The following instructions assume you’re using Windows PowerShell.
The project was developed with Flask and standard Python tooling.

🧱 Prerequisites

Python 3.10+ installed and added to your PATH

git (optional, for cloning the repository)

🐍 Create and Activate a Virtual Environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

📦 Install Dependencies
pip install -r requirements.txt


If requirements.txt is missing, install Flask manually:

pip install Flask

▶️ Run the App (Development)

From the project root:

set FLASK_APP=app.py; set FLASK_ENV=development; flask run


Then open http://127.0.0.1:5000
 in your browser.

🧪 Run Tests

This project includes a simple pytest test file: test_app.py.

pip install pytest
pytest -q

📁 Project Structure
├── app.py               # Flask application and routes
├── templates/           # Jinja2 templates (base.html, home.html, symp_checker.html)
├── static/              # Static assets (CSS, images)
└── test_app.py          # Basic tests for the home route

🤝 Contributing

Contributions are welcome!
If you add features that interact with external AI or medical APIs, do not commit API keys or secrets.
Use environment variables or a local config file excluded from version control.
