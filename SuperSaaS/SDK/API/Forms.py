from .BaseApi import BaseApi


class Forms(BaseApi):
    def get(self, form_id):
        path = "/forms.json"

    def find(self, form_id, from_time=None):
        path = "/forms.json"
