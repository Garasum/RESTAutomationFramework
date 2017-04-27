import requests
import pytest
from main.Response_Codes import SUCCESS
from main.Ulrs import USERS


def test_get_all_users():
    response = requests.get(USERS)
    print()
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Text:", response.text)
    assert response.status_code == SUCCESS
