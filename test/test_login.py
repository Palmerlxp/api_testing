import requests
import json
from rich import print
import pytest
from parameters import api_test_login

class TestLogin(object):

    @pytest.mark.parametrize('email,password',api_test_login.test_login_data)
    def test_login(self,email,password):
        res = requests.post('http://192.168.2.242:8000/api/authenticaion/login', json={
                "user": {
                    "email": email,
                    "password": password
                }
            })
        print(json.loads(res.content))
        print(res.status_code)
        assert True