from flask_app import app
from flask_app.controllers import users, recipes

# ALWAYS IMPORT YOUR CONTROLLERSS IN server.py
# import app from init.py(flask_app)

if __name__=="__main__":     
    app.run(debug=True)


    