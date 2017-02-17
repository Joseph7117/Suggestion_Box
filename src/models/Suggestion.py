import uuid
import datetime
from src.common.Database import Database


class Suggestions(object):
    def __init__(self,board_id, author, title, description, date=datetime.datetime.utcnow(), _id=None):
        self.author = author
        self.board_id = board_id
        self.title = title
        self.description = description
        self.created_date = date
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return{
            "board_id": self.board_id,
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "created_date": self.created_date,
            "id": self._id
        }
    def save_to_db(self):
        Database.insert_data("suggest", self.json())

    @staticmethod
    def fetch_suggestions():
        return [suggestions for suggestions in Database.find("suggest", {})]

    @staticmethod
    def fetch_by_id(brd_id):
        return [suggestion_title for suggestion_title in Database.find("suggest", {"board_id": brd_id})]

    #detach suggestion when it gets past three reactions
    @staticmethod
    def delete(brd_id):
        return [sugg_ttle for sugg_ttle in Database.remove("suggest", {"board_id": brd_id})]
