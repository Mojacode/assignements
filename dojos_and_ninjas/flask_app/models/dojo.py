from flask_app.config.mysqlconnection import connectToMySQL

# import Ninja class from ninja.py(model) to used later with a classmethod
from flask_app.models.ninja import Ninja
# this is a model(name is singular)
# CONTAINS CLASS METHODS FOR Dojos
class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

# get all the names of the Dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos_ninjas.dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_ninjas').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
                dojos.append( cls(dojo) )
        return dojos

# get a certain dojo with all the ninjas associated with it
    @classmethod
    def get_one_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(n))
        return dojo

# add a new dojo to the database
    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos_ninjas.dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())"
        return connectToMySQL('dojos_ninjas').query_db(query,data)




# INSERT INTO dojos_ninjas.ninjas (first_name, last_name, age, dojos_id, created_at, updated_at) VALUES (%(first_name)s, %(first_name)s ,%(age)s, %(dojos_id)s, NOW(), NOW())
