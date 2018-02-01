from .BaseApi import BaseApi


class Users(BaseApi):
    def get(self, user_id=None, form=None, limit=None, offset=None):
        pass

    def create(self, attributes, user_id=None):
        pass

    def update(self, user_id, attributes):
        pass

    def delete(self, user_id):
        pass
