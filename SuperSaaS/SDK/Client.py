import threading

from .Error import Error

API_VERSION  = '1'
VERSION = '0.1.0'

class Client(object):
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
      if not cls.__singleton_instance:
        with cls.__singleton_lock:
          if not cls.__singleton_instance:
            cls.__singleton_instance = cls()
      return cls.__singleton_instance
    

    def __init__(self, configuration):
      self.account_name = configuration.account_name
      self.user_name = configuration.user_name
      self.password = configuration.password
      self.host = configuration.host
      self.test = configuration.test

class Configuration(object)
    def __init__(self):
      self.account_name = ''
      self.user_name = ''
      self.password = ''
      self.host = 'http://localhost:3000'
      self.test = False
