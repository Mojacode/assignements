from flask_app.config.mysqlconnection import connectToMySQL

# this is a model(name is singular)
# CONTAINS CLASS METHODS FOR Dojos

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# this will save a new ninja 
    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO dojos_ninjas.ninjas (first_name, last_name, age, dojos_id, created_at, updated_at) VALUES (%(fname)s, %(lname)s ,%(age)s, %(dojo)s, NOW(), NOW())"
        return connectToMySQL('dojos_ninjas').query_db(query,data)
