from .BaseApi import BaseApi
from ..Models.Appointment import Appointment
from ..Models.Slot import Slot


class Appointments(BaseApi):
    def agenda(self, schedule_id, user_id, from_time=None, slot=None):
        path = "/agenda/{}.json".format(self._validate_id(schedule_id))
        params = {
            'user': user_id,
            'from': self._validate_datetime(from_time) if from_time else None,
            'slot': 'true' if slot else None
        }
        res = self.client.request('GET', path, params)
        return self.__map_slots_or_bookings(res, slot)

    def available(self, schedule_id, from_time=None, length_minutes=None, resource=None, full=None, limit=None):
        path = "/free/{}.json".format(self._validate_id(schedule_id))
        params = {
            'length_minutes': self._validate_number(length_minutes) if length_minutes else None,
            'from': self._validate_datetime(from_time) if from_time else None,
            'resource': resource,
            'full': 'true' if full else None,
            'limit': self._validate_number(limit) if limit else None
        }
        res = self.client.request('GET', path, params)
        return self.__map_slots_or_bookings(res)

    def get(self, schedule_id, appointment_id=None, form=None, start_time=None, limit=None):
        if appointment_id:
            params = {schedule_id: self._validate_id(schedule_id)}
            path = "/bookings/{}.json".format(self._validate_id(appointment_id))
            res = self.client.request('GET', path, params)
            return Appointment(res)
        else:
            path = "/bookings.json"
            params = {
                'schedule_id': self._validate_id(schedule_id),
                'form': 'true' if form else None,
                'start': self._validate_datetime(start_time) if start_time else None,
                'limit': self._validate_number(limit) if limit else None
            }
            res = self.client.request('GET', path, params)
            return self.__map_slots_or_bookings(res)

    def create(self, schedule_id, user_id, attributes, form=None, webhook=None):
        path = "/bookings.json"
        params = {
            'schedule_id': schedule_id,
            'webhook': webhook,
            'user_id': self._validate_id(user_id),
            'form': attributes['form'],
            'booking': {
                'start': attributes['start'],
                'finish': attributes['finish'],
                'name': self._validate_present(attributes['name']),
                'email': attributes['email'],
                'full_name': attributes['full_name'],
                'address': attributes['address'],
                'mobile': attributes['mobile'],
                'phone': attributes['phone'],
                'country': attributes['country'],
                'field_1': attributes['field_1'],
                'field_2': attributes['field_2'],
                'field_1_r': attributes['field_1_r'],
                'field_2_r': attributes['field_2_r'],
                'super_field': attributes['super_field'],
                'resource_id': attributes['resource_id'],
                'slot_id': attributes['slot_id']
            }
        }
        res = self.client.request('POST', path, params)
        return Appointment(res)

    def update(self, schedule_id, appointment_id, attributes, webhook=None):
        path = "/bookings/{}.json".format(self._validate_id(appointment_id))
        params = {
            'schedule_id': schedule_id,
            'webhook': webhook,
            'form': attributes['form'],
            'booking': {
                'start': attributes['start'],
                'finish': attributes['finish'],
                'name': self._validate_present(attributes['name']),
                'email': attributes['email'],
                'full_name': attributes['full_name'],
                'address': attributes['address'],
                'mobile': attributes['mobile'],
                'phone': attributes['phone'],
                'country': attributes['country'],
                'field_1': attributes['field_1'],
                'field_2': attributes['field_2'],
                'field_1_r': attributes['field_1_r'],
                'field_2_r': attributes['field_2_r'],
                'super_field': attributes['super_field'],
                'resource_id': attributes['resource_id'],
                'slot_id': attributes['slot_id']
            }
        }
        res = self.client.request('PUT', path, params)
        return Appointment(res)

    def delete(self, appointment_id):
        path = "/bookings/{}.json".format(self._validate_id(appointment_id))
        return self.client.request('DELETE', path)

    def changes(self, schedule_id, from_time=None, slot=False):
        path = "/changes/{}.json".format(self._validate_id(schedule_id))
        params = {
            'from': self._validate_datetime(from_time) if from_time else None,
            'slot': 'true' if slot else None
        }
        res = self.client.request('GET', path, params)
        return self.__map_slots_or_bookings(res, slot)

    def __map_slots_or_bookings(self, obj, slot=False):
        if slot:
            return [Slot(attributes) for attributes in obj.get('slots', [])]
        else:
            return [Appointment(attributes) for attributes in obj.get('bookings', [])]
