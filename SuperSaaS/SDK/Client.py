import sys
import threading

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError

try:
    import json
except ImportError:
    import simplejson as json

from base64 import b64encode

from . import API
from .Error import Error

PYTHON_VERSION = '.'.join(sys.version_info)
API_VERSION = '1'
VERSION = '0.1.0'


class Client(object):
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls(Configuration())
        return cls.__singleton_instance

    @classmethod
    def configure(cls, account_name, password, user_name, test=False, host=None):
        cls.instance().account_name = account_name
        cls.instance().password = password
        cls.instance().user_name = user_name
        cls.instance().test = test
        cls.instance().test = host or cls.instance().host

    @classmethod
    def _user_agent(self):
        return "SSS/{} Python/{} API/{}".format(VERSION, PYTHON_VERSION, API_VERSION)

    def __init__(self, configuration):
        self.account_name = configuration.account_name
        self.user_name = configuration.user_name
        self.password = configuration.password
        self.host = configuration.host
        self.test = configuration.test

        self.appointments = API.Appointments(self)
        self.forms = API.Forms(self)
        self.users = API.Users(self)

        self.last_request = None

    def request(self, http_method, path, params=None, query=None):
        if params is None:
            params = {}
        if query is None:
            query = {}

        if not self.account_name:
            raise Error("Account name not configured. Call `SuperSaaS.Client.configure`.")
        if not self.password:
            raise Error("Account password not configured. Call `SuperSaaS.Client.configure`.")

        auth = b64encode('{}:{}'.format(self.account_name, self.password))
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': self._user_agent(),
            'Authorization': "Basic {}".format(auth)
        }

        url = "{}/api/{}".format(self.host, path)
        if http_method == 'GET':
            query = params
            params = None
        if query:
            querystring = urlencode(query)
            url = "{}?{}".format(url, querystring)

        data = dict(filter(lambda item: item[1] is not None, params.items()))
        data = json.dumps(data)
        req = Request(url, data, headers)

        if http_method == 'GET':
            req.get_method = http_method
        elif http_method == 'POST':
            req.get_method = http_method
        elif http_method == 'PUT':
            req.get_method = http_method
        elif http_method == 'DELETE':
            req.get_method = http_method
        else:
            raise Error("Invalid HTTP Method: {}. Only `GET`, `POST`, `PUT`, `DELETE` supported.".format(http_method))

        self.last_request = req

        try:
            res = urlopen(req)
            data = json.load(res.read())
            return data
        except HTTPError, e:
            raise Error("HTTP Request Error ({}): {}".format(url, e.reason))


class Configuration(object):
    def __init__(self):
        self.account_name = ''
        self.user_name = ''
        self.password = ''
        self.host = 'http://localhost:3000'
        self.test = False
