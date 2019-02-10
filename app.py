from flask import Flask, render_template
from data import notesData
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators 
from passlib.hash import sha256_crypt

app = Flask(__name__)

# config mysql
app.config('MYSQL_HOST') = 'localhost'
app.config('MYSQL_USER') = 'root'
app.config('MYSQL_PASSWORD') = '12345678'
app.config('MYSQL_DB') = 'tnrapp'
app.config('MYSQL_CURSORCLASS') = 'DictCursor'

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

        flash("You have successfully registered and can can login.", 'success')
        redirect(url_for('home'))

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug = True)

