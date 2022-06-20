
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt 
from flask import flash   

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under30 = data['under30']
        self.datemade = data['datemade']
        self.users_id = data['users_id']
        
    @classmethod
    def save_recipe(cls,data):
        query = "INSERT INTO recipes (name, description, instruction , under30, datemade , users_id, created_at, updated_at) VALUES (%(name)s,%(description)s,%(instruction)s ,%(under30)s, %(datemade)s, %(users_id)s, NOW(),NOW());"
        return connectToMySQL("register").query_db(query, data)
    
    @classmethod
    def get_all(cls, data):
        query = "SELECT * from recipes;"
        results = connectToMySQL("register").query_db(query,data)
        all_recipes = []
        for recipe in results:
            print(recipe)
            all_recipes.append(cls(recipe))
        return all_recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * from recipes WHERE id = %(id)s;"
        results = connectToMySQL("register").query_db(query,data)
        return cls(results[0])





