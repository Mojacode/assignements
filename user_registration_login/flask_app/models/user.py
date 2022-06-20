
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt 
from flask import flash   
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app) 
# this is a model(name is singular)
# CONTAINS CLASS METHODS FOR users

# class User:
#     def __init__(self, data):
        


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']



    @staticmethod
    def validate_register(user):
        # connect to db to check for existing user
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("register").query_db(query,user)

        # Validation
        is_valid = True # we assume this is true
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(user['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 8:
            flash("Email must be at least 8 characters.")
            is_valid = False
        if len(user['password']) < 3:
            flash("Password must be at least 3 characters.")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Password does not match")
            is_valid = False
        return is_valid
    
    @classmethod
    def validate_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("register").query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    






    @classmethod
    def get_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("register").query_db(query,data)
        return cls(results[0])


    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s, NOW(),NOW());"
        return connectToMySQL("register").query_db(query, data)