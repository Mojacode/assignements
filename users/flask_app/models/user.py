from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_schema.users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users_schema.users WHERE users.id=%(id)s"
        results = connectToMySQL('users_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users_schema.users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s,%(lname)s,%(email)s, NOW(), NOW())"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def edit_user(cls,data):
        query = "UPDATE users_schema.users SET first_name = %(fname)s, last_name = %(lname)s, email= %(email)s,updated_at= NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users_schema.users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

