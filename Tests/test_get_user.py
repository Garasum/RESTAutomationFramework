import requests
import pytest
from main.Response_Codes import SUCCESS
from main.Ulrs import USERS, USER_BY_USERNAME


def test_get_user():
    # r = requests.post('http://httpbin.org/post', data={'key': 'value'})
    name = "bob"
    response = requests.get(USER_BY_USERNAME.format(name))
    print()
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Text:", response.text)
    assert response.status_code == SUCCESS
    # assert response.text == name
