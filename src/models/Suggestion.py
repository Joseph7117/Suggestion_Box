import uuid


class Suggestions(object):
    def __init__(self, title, description, _id=None):
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return{
            "title": self.title,
            "description": self.description,
            "id": self._id
        }