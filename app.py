from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy database of users and medicines
users = {'vivek': '123', 'kuldeep': '456'}
medicines = {
    'fever': 'Paracetamol',
    'head pain': 'Asprin',
    'cold': 'Cetirizine',
    'headache': 'Aspirin',
    'cough': 'Cough Syrup',
    'stomach ache': 'Omeprazole'
}

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('recommendation'))
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

# Recommendation route
@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    if 'username' in session:
        if request.method == 'POST':
            condition = request.form['condition'].lower()
            medicine = medicines.get(condition, 'No recommendation available for this condition')
            return render_template('recommendation.html', medicine=medicine)
        return render_template('recommendation.html', medicine=None)
    return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
