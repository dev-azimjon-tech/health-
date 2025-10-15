from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
   return render_template("home.html")


@app.route("/symp_checker")
def symp_checker():
   return render_template("symp_checker.html")
if __name__ == "__main__":
    app.run(debug=True)