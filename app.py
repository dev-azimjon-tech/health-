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

if __name__ == '__main__':
    app.run(debug=True)
