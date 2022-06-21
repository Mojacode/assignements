
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods =['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    pw_hash= bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "password": pw_hash,
        "email": request.form['email']
        }

    user_id = User.save(data)
    session['id'] = user_id
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
    user= User.validate_email(request.form)

    if not user:
        flash("Email Not Found")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']  
    }
    return render_template('dashboard.html', user = User.get_id(data), recipes = Recipe.get_all(data) )

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')