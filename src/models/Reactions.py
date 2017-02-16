import datetime
import uuid

from src.common.Database import Database


class Reactions(object):
    def __init__(self, suggestion_id, author, comment, date=datetime.datetime.utcnow(), upvote=0, downvote=0, flagged=0, _id=None):
        self.suggestion_id = suggestion_id,
        self.author = author,
        self.comment = comment,
        self.date = date,
        self.upvote = upvote,
        self.downvote = downvote,
        self.flagged = flagged,
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            "suggestion_id": self.suggestion_id,
            "author": self.author,
            "comment": self.comment,
            "date": self.date,
            "upvote": self.upvote,
            "downvote": self.downvote,
            "flagged": self.flagged,
            "id": self._id
        }

    @staticmethod
    def fetch_reaction(brd_id):
        return [react for react in Database.find("reactions", {"suggestion_id": brd_id})]

    def save_to_db(self):
        Database.insert_data("reactions", self.json())

    @staticmethod
    def fetch_upvotes(brd_id):
        return [upreact for upreact in Database.find("reactions", {"suggestion_id": brd_id, "upvote": "on"})]

    @staticmethod
    def fetch_downvotes(brd_id):
        return [downreact for downreact in Database.find("reactions", {"suggestion_id": brd_id, "downvote": "on"})]

    @staticmethod
    def fetch_flagged_bad(brd_id):
        return [flagged for flagged in Database.find("reactions", {"suggestion_id": brd_id, "flagged": "on"})]
