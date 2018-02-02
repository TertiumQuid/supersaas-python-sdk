import unittest
from SuperSaaS import SDK


class SupersaasTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        self.__fileName = ""
        self.__file = None

        self.config = SDK.Configuration()
        self.client = SDK.Client(self.config)
        self.client.account_name = 'test'
        self.client.password = 'test'
        self.client.test = True
