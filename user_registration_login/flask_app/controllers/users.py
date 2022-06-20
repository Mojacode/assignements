

from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    if not User.validate_register(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "password" : pw_hash,
        "email": request.form['email'],

    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/")



@app.route('/login', methods = ['POST'])
def login():
    user = User.validate_email(request.form)

    if not user:
        flash("Email Not Found")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid password")
        return redirect('/')
    session['id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'id' not in session:
        return redirect ('/')
    data = {
        'id' : session["id"]
    }
    return render_template('user.html', user=User.get_id(data))



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')