import requests

from main.Response_Codes import SUCCESS
from main.Ulrs import HELLO


def get_hello():
    response = requests.get(HELLO)
    print("Status Code: ", response.status_code)
    print("Text: ", response.text)
    assert response.status_code == SUCCESS


if __name__ == '__main__':
    get_hello()
