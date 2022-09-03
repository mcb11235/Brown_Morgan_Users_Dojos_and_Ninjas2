from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = []
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        users = []
        for dojo in results:
            users.append(cls(dojo))
        return users
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
    @classmethod
    def get_one(cls, data):
        query = """SELECT * FROM dojos
        JOIN ninjas ON ninjas.dojo_id = dojos.id
        WHERE dojos.id=%(id)s;
         """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls( results[0] )
        print(results[0])
        for row_from_db in results:
            print(row_from_db["id"])
            user_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name": row_from_db['first_name'],
                "last_name": row_from_db['last_name'],
                "age": row_from_db["age"],
                "dojo_id": row_from_db['dojo_id'],
                "created_at": row_from_db['ninjas.created_at'],
                "updated_at": row_from_db['ninjas.updated_at'],                                
            }
            dojo.users.append(User(user_data))
        return dojo
  
