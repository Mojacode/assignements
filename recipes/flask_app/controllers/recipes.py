
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


# route to recipe form
@app.route('/add')
def new_recipe():
    if 'id' not in session:
        return redirect('/')
    data = {
        "id":session['id']
    }
    return render_template('addrecipe.html', user=User.get_id(data))




@app.route("/add_recipe", methods=["POST"])
def add_recipe():
    
    if 'id' not in session:
        return redirect ('/')

    data={
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "under30" : request.form['under30'],
        "datemade": request.form['datemade'],
        "users_id": session['id']
    }
    Recipe.save_recipe(data)
    return redirect('/dashboard')

@app.route('/show/recipe/<int:recipe_id>')
def show_recipe(recipe_id):
    data={
        'id': recipe_id
    }
    return render_template('showrecipe.html', recipe = Recipe.get_one(data))
