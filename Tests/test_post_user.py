import requests
import pytest
from main.Response_Codes import SUCCESS
from main.Ulrs import USERS


def test_post_user():
    # r = requests.post('http://httpbin.org/post', data={'key': 'value'})
    # data = {"name": "bob"}
    data = "zzzz"
    response = requests.post(USERS, data)
    print()
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Text:", response.text)
    assert response.status_code == SUCCESS
    assert response.text.__contains__("ok")
