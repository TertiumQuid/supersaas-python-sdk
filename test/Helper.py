import unittest

class SupersaasTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__fileName = ""
        self.__file = None