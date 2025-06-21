from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    illnesses = [
        {'title': 'Кашель', 'solution': 'Отдых, лёд, компрессия', 'image': 'doctor.png'},
        {'title': 'Кашель', 'solution': 'Пейте больше жидкости', 'image': 'cough.png'},
        {'title': 'Жар', 'solution': 'Примите жаропонижающие', 'image': 'fever.png'}
    ]
    return render_template('home.html', illnesses=illnesses)

@app.route('/chat_ai')
def chat_ai():
    return render_template('chat_ai.html')

@app.route('/heart_problems')
def heart_problems():
    return render_template('health_category/heart_problems/heart_problems.html')

if __name__ == '__main__':
    app.run(debug=True)
