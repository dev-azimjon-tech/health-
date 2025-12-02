from flask import Flask, render_template, request, redirect, url_for, session, flash
import hashlib

app = Flask(__name__)
app.secret_key = '312803237490827390573418957314895701734'  # Change this to a secure random value

# --- Mini "database" ---
users_db = {}  # Format: {username: {'password': hashed_password, 'email': email}}
admin_db = {}
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm', '')

        if not username or not email or not password or not confirm:
            flash('Please fill in all fields.', 'danger')
        elif '@' not in email or '.' not in email:
            flash('Please enter a valid email address.', 'danger')
        elif password != confirm:
            flash('Passwords do not match.', 'danger')
        elif username in users_db:
            flash('Username already exists.', 'danger')
        else:
            users_db[username] = {'password': hash_password(password), 'email': email}
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = users_db.get(username)
        if user and user['password'] == hash_password(password):
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out.', 'info')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)