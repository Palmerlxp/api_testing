import json
import requests
import pytest
from rich import print
from parameters import api_test_register

@pytest.mark.parametrize('email,password,username', api_test_register.test_register_data)
def test_register(email, password, username):
    res = requests.post('http://192.168.2.242:8000/api/authenticaion/register', json={
  "user": {
    "email": email,
    "password": password,
    "username": username
  }
})
    print(json.loads(res.content))
    print(res.status_code)
    assert True

