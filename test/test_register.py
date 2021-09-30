import json
import requests
import pytest
from rich import print

test_register_data = [('testPalmer01@example.com', 'dsad','testPalmer01'), ('testPalmer02@qq.com','dsada','testPalmer02')]
@pytest.mark.parametrize('email,password,username', test_register_data)
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

