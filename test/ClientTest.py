from .Helper import *
from SuperSaaS import SDK


class ClientTest(SupersaasTest):

    def test_api(self):
        self.assertIsNotNone(self.client.appointments)
        self.assertIsNotNone(self.client.forms)
        self.assertIsNotNone(self.client.users)

    def test_request(self):
        for method in ['GET', 'POST', 'PUT', 'DELETE']:
            self.assertIsNotNone(self.client.request(method, '/test', {'test': True}))

    def test_instance_configuration(self):
        self.client.configure(account_name='account', password='password', user_name='user')
        self.assertEqual('account', SDK.Client.instance().account_name)
        self.assertEqual('password', SDK.Client.instance().password)
        self.assertEqual('user', SDK.Client.instance().user_name)
