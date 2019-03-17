from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import notesData
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators 
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

# config mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'tnrapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init mysql
mysql = MySQL(app)

# init notesData
notesData = notesData()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/all-notes')
def allnotes():
    return render_template('all-notes.html')

# not done:
@app.route('/all-notes/<string:id>/')
def note(id):
    return render_template('note.html', id=id)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/view-notes')
def viewNotes():
    return render_template('view-notes.html')

# linked by all-notes
@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/validate-notes')
def validateNotes():
    return render_template('validate-notes.html')

@app.route('/terms-cond')
def termsCond():
    return render_template('terms-cond.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
        # commit to DB
        mysql.connection.commit()
        # close connection 
        cur.close()

        flash("You have successfully registered and can login.", 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=1, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form fields
        username = request.form['username']
        password_candidate = request.form['password']
        
        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('home'))
            else:
                error = 'Wrong password'
                return render_template('login.html', error=error)
            cur.close()

        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
    return render_template('login.html')

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to be logged in to access this page.', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug = True)

