from .BaseApi import BaseApi
from ..Models.Form import Form


class Forms(BaseApi):
    def get(self, form_id):
        path = "/forms.json"
        params = {
            'form_id': self._validate_id(form_id)
        }
        res = self.client.request('GET', path, params)
        return [Form(attributes) for attributes in res]

    def find(self, form_id, from_time=None):
        path = "/forms.json"
        params = {
            'id': self._validate_id(form_id)
        }
        if from_time:
            params['from_time'] = self._validate_datetime(from_time)
        res = self.client.request('GET', path, params)
        return Form(res)
