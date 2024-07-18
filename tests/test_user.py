import requests


import requests


def get_token(username, password):
    response = requests.post('http://localhost/docs#/Authentication/login_for_access_token_token_post', json={"user": username, "pass123": password})
    return response.json().get("token")

# def test_create_user():
#     response = requests.post('http://localhost/docs#/Users/get_users_users__get', json={"username": "test_user", "password": "test_pass"})
#     assert response.status_code == 201


