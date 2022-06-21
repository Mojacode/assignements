
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


# route to recipe form
@app.route('/add')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id":session['user_id']
    }
    return render_template('addrecipe.html', user=User.get_id(data))

@app.route('/delete/<int:id>')
def delete(id):

    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    Recipe.delete(data)
    return redirect('/dashboard')




@app.route("/add_recipe", methods=["POST"])
def add_recipe():
    
    if 'user_id' not in session:
        return redirect ('/')

    data={
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "under30" : request.form['under30'],
        "datemade": request.form['datemade'],
        "users_id": session['user_id']
    }
    Recipe.save_recipe(data)
    return redirect('/dashboard')

@app.route('/show/recipe/<int:recipe_id>')
def show_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect ('/')
    data={
        'id': recipe_id
    }
    return render_template('showrecipe.html', recipe = Recipe.get_one(data))

@app.route('/show/edit/<int:recipe_id>')
def edit_form(recipe_id):
    if 'user_id' not in session:
        return redirect ('/')

    data={
        "id" : recipe_id
    }
    return render_template('editrecipe.html', recipe= Recipe.get_one(data))

@app.route("/show/edit_recipe", methods=["POST"])
def update_recipe():
    
    if 'user_id' not in session:
        return redirect ('/')

    data={
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "under30" : request.form['under30'],
        "datemade": request.form['datemade'],
        "id": request.form['id']
    }
    Recipe.update_recipe(data)
    return redirect('/dashboard')


