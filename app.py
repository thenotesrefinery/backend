from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import notesData
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators 
from passlib.hash import sha256_crypt

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

@app.route('/verify')
def verify():
    return render_template('verify.html')

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
        redirect(url_for('home'))

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

if __name__ == '__main__':
    app.run(debug = True)

