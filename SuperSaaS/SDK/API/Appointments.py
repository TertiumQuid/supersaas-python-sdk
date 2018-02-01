from .BaseApi import BaseApi


class Appointments(BaseApi):
    def agenda(self, schedule_id, user_id, from_time=None, slot=None):
        pass

    def available(self, schedule_id, from_time=None, length_minutes=None, resource=None, full=None, limit=None):
        pass

    def get(self, schedule_id, appointment_id=None, form=None, start=None, limit=None):
        pass

    def create(self, schedule_id, user_id, attributes, form=None, webhook=None):
        pass

    def update(self, schedule_id, appointment_id, attributes):
        pass

    def delete(self, appointment_id):
        pass

    def changes(self, schedule_id, from_time=None, slot=None):
        pass
