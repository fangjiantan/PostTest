#conding: utf-8

import unittest
import json
import traceback
import requests
import time
import config as cf



class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_url = 'http://api.chebaotec.com/washingmanage/n/login'
        cls.headers = {"KEY":"Content-Type","VALUE":"application/json"}
        cls.data = {"account":"admin","password":"yingshitec2018@"}

    def test_login(self):
        response = requests.post(self, self.login_url)





