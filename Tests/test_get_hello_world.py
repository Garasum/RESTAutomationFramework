import requests
import pytest
from main.Response_Codes import SUCCESS
from main.Ulrs import HELLO


def test_get_hello_world():
    response = requests.get(HELLO)
    print()
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Text:", response.text)
    assert response.status_code == SUCCESS
