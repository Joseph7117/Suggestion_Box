'''
Defining the User Model
'''
import uuid

from flask import session

from src.common.Database import Database

class User(object):

    def __init__(self, name, email, password, _id=None):
        self.name = name
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_id(cls, id):
        data = Database.find_one("users", {"_id": id})
        if data is not None:
            return User(data["email"], data["password"])

    @classmethod
    #Object will not be instiated while finding the user
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return User(data["name"], data["email"], data["password"])

    @staticmethod
    def is_login_valid(email, password):
        #Check if user's email matches the password they keyed in
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password
        return False

    @classmethod
    def register_user(cls, name, email, password):
        user = User.get_by_email(email)
        if user is None:
            #Create the User since he/she does not exist in the database
            new_user = User(name, email, password)
            new_user.save_to_db()
            session['name'] = name
            session['email'] = email
            return True
        else:
            #The user exists in our Database
            return False

    @staticmethod
    def login(email):
        #Store User's information in a Session if after verification ie. is_login_valid()
        session['email'] = email

    @staticmethod
    def logout():
        session['email'] = None

    #Getting suggestions for a specific user_id
    def get_suggestions(self):
        pass

    def json(self) -> object:
        return{
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "_id": self._id
        }
    def save_to_mongo(self):
        Database.insert_data("users", self.json())
