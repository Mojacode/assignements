from flask import render_template, request, redirect, session
from flask_app import app

# import the models to your controller so you can use the classmethods contained in the models
from flask_app.models.dojo import Dojos
from flask_app.models.ninja import Ninja


# this is a controller(name is plural)
# Contains routes


@app.route('/ninja')
def show_ninja():
    dojo = Dojos.get_all()
    return render_template("ninja.html", dojo = dojo)

@app.route("/add/ninja", methods=['POST'])
def add_ninja():
    print(request.form)
    Ninja.save_ninja(request.form)
    return redirect('/')