
from flask import render_template, request, redirect, session
from flask_app import app

# import the models to your controller so you can use the classmethods contained in the models
from flask_app.models.dojo import Dojos
# this is a controller(name is plural)
# Contains routes

@app.route('/')
def index():
    dojos = Dojos.get_all()
    print(dojos)
    return render_template("index.html" ,dojos = dojos )

# ADDS NEW DOJO
@app.route('/add', methods=['POST'])
def add_dojo():
    data = {
        'name': request.form['dojoname']
    }
    Dojos.add_dojo(data)
    return redirect ('/')

#RENDERS SHOW DOJO INFO
@app.route('/showdojo/<int:id>')
def show_dojo(id):
    data={
        'id': id
    }
    return render_template("showdojo.html", dojo=Dojos.get_one_with_ninjas(data))


