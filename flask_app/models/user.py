from flask_app.config.mysqlconnection import connectToMySQL
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id ) VALUES ( %(fname)s , %(lname)s , %(age)s , %(dojo_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(results[0])
    @classmethod
    def update(cls, data):
        print(data)
        query = "UPDATE users SET first_name=%(fname)s,last_name=%(lname)s,email=%(email)s,updated_at=NOW() WHERE id=%(id)s;"
        print(query)
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
