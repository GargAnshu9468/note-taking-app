import requests


def test_register(url, json):
    return requests.post(url=url, json=json)


def test_login(url, data):
    return requests.post(url=url, data=data)


def test_users_me(url, headers):
    return requests.get(url=url, headers=headers)


def test_create_note(url, headers, json):
    return requests.post(url=url, headers=headers, json=json)


def test_get_note_by_id(url, headers):
    return requests.get(url=url, headers=headers)


def test_get_notes(url, headers):
    return requests.get(url=url, headers=headers)


def test_update_note_by_id(url, headers, json):
    return requests.put(url=url, headers=headers, json=json)


def test_delete_note_by_id(url, headers):
    return requests.delete(url=url, headers=headers)


BASE_URL = 'http://localhost:8000'
USERS_ME_ENDPOINT = '/users/me'
REGISTER_ENDPOINT = '/register'
LOGIN_ENDPOINT = '/login'
NOTES_ENDPOINT = '/notes'

user_data = {
    'username': 'garganshu',
    'password': 'garganshu'
}

response = test_register(f'{BASE_URL}{REGISTER_ENDPOINT}', user_data)
print(f"\nRESPONSE :: {response.json()}\n")

response = test_login(f'{BASE_URL}{LOGIN_ENDPOINT}', user_data)
json_response = response.json()

access_token = json_response.get('access_token', '')
print(f"\nAccess Token :: {access_token}\n")

headers = {
    'Authorization': f'Bearer {access_token}'
}

response = test_users_me(f'{BASE_URL}{USERS_ME_ENDPOINT}', headers)
print(f"\nRESPONSE :: {response.json()}\n")

note_data = {
    "title": "Python",
    "content": "Python is a high-level, general-purpose programming language."
}

response = test_create_note(f'{BASE_URL}{NOTES_ENDPOINT}', headers, note_data)

note_id = response.json()
print(f"\nNote ID :: {note_id}\n")

response = test_get_note_by_id(f'{BASE_URL}{NOTES_ENDPOINT}/{note_id}', headers)
print(f"\nNote :: {response.json()}\n")

response = test_get_notes(f'{BASE_URL}{NOTES_ENDPOINT}', headers)
print(f"\nNotes :: {response.json()}\n")

note_data = {
    "title": "FastAPI",
    "content": "FastAPI is a modern web framework first released in 2018 for building RESTful APIs in Python."
}

response = test_update_note_by_id(f'{BASE_URL}{NOTES_ENDPOINT}/{note_id}', headers, note_data)
print(f"\nRESPONSE :: {response.json()}\n")

response = test_delete_note_by_id(f'{BASE_URL}{NOTES_ENDPOINT}/{note_id}', headers)
print(f"\nRESPONSE :: {response.json()}\n")
