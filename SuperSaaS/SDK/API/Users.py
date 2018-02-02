from .BaseApi import BaseApi
from ..Models.User import User


class Users(BaseApi):
    def get(self, user_id=None, form=None, limit=None, offset=None):
        path = self.__user_path(user_id)
        if user_id:
            res = self.client.request('GET', path)
            return User(res)
        else:
            params = {
                'form': form == True if form else None,
                'limit': self._validate_number(limit) if limit else None,
                'offset': self._validate_number(offset) if offset else None
            }
            res = self.client.request('GET', path, params)
            return [User(attributes) for attributes in res]

    def create(self, attributes, user_id=None):
        path = self.__user_path(user_id)
        params = {
            'webhook': attributes['webhook'],
            'user': {
                'name': self._validate_present(attributes['name']),
                'email': attributes['email'],
                'password': attributes['password'],
                'full_name': attributes['full_name'],
                'address': attributes['address'],
                'mobile': attributes['mobile'],
                'phone': attributes['phone'],
                'country': attributes['country'],
                'field_1': attributes['field_1'],
                'field_2': attributes['field_2'],
                'super_field': attributes['super_field'],
                'credit': self._validate_number(attributes['credit']) if attributes['credit'] else None,
                'role': self._validate_options(attributes['role'], [3, 4, -1]) if attributes['role'] else None
            }
        }
        res = self.client.request('POST', path, params)
        return User(res)

    def update(self, user_id, attributes):
        path = self.__user_path(user_id)
        params = {
            'webhook': attributes['webhook'],
            'user': {
                'name': self._validate_present(attributes['name']),
                'email': attributes['email'],
                'password': attributes['password'],
                'full_name': attributes['full_name'],
                'address': attributes['address'],
                'mobile': attributes['mobile'],
                'phone': attributes['phone'],
                'country': attributes['country'],
                'field_1': attributes['field_1'],
                'field_2': attributes['field_2'],
                'super_field': attributes['super_field'],
                'credit': self._validate_number(attributes['credit']) if attributes['credit'] else None,
                'role': self._validate_options(attributes['role'], [3, 4, -1]) if attributes['role'] else None
            }
        }
        return self.client.request('PUT', path, params)

    def delete(self, user_id):
        path = self.__user_path(self._validate_id(user_id))
        return self.client.request('DELETE', path)

    def __user_path(self, id):
        return "/users/{}.json".format(id) if id else "/users.json"
