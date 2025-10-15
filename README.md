# Health-

A small web application for checking symptoms using an AI-backed symptom checker.

This project provides a minimal UI where users can check symptoms and (in future) search for drug information. It is intended as a prototype / demo and is not a substitute for professional medical advice.

Key features

- No user registration required — users can check symptoms without creating an account.
- AI symptom checker (integration point for a medical LLM or external API such as Gemini).
- Drug search (placeholder for drug lookup features).
- Minimal, mobile-friendly UI built with Flask templates and Tailwind CSS.
- Optional premium / optimized model support (conceptual).

 Notes
 
 New: A minimal AI Chat demo is available at the `/chat` route. It uses a local mock endpoint (`/api/chat`) which you can replace with a real AI service.

- This repository is an educational/demo project. Do not rely on it for medical diagnosis.

## Developer setup

These instructions assume you are on Windows and using PowerShell (the project was developed with Flask and standard Python tooling).

Prerequisites

- Python 3.10+ installed and available on PATH.
- git (optional, for cloning the repository).

Create and activate a virtual environment (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies

```powershell
pip install -r requirements.txt
```

If the `requirements.txt` file is missing, install Flask directly:

```powershell
pip install Flask
```

Run the app (development)

```powershell
# from the project root
set FLASK_APP=app.py; set FLASK_ENV=development; flask run
```

Open http://127.0.0.1:5000 in your browser.

Run tests

This project includes a simple pytest test file `test_app.py`.

```powershell
pip install pytest
pytest -q
```

Project layout

- `app.py` — Flask application and routes.
- `templates/` — Jinja2 templates used by the app (`base.html`, `home.html`, `symp_checker.html`).
- `static/` — static assets (CSS, images).
- `test_app.py` — basic tests for the home route.

Contributing

- Feel free to open issues or PRs. When adding features that call external AI or medical APIs, ensure you do not commit API keys or secrets. Use environment variables or a local config file ignored by git.

License

Add a license file (e.g., `LICENSE`) if you want to publish or share this project publicly.
---
