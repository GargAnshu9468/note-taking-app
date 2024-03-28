import requests


def test_create_note(url, headers, json):
    return requests.post(url=url, headers=headers, json=json)


def test_get_note_by_id(url, headers, note_id):
    return requests.get(url=f"{url}/{note_id}", headers=headers)


def test_get_notes(url, headers):
    return requests.get(url=url, headers=headers)


def test_update_note_by_id(url, headers, note_id, json):
    return requests.put(url=f"{url}/{note_id}", headers=headers, json=json)


def test_delete_note_by_id(url, headers, note_id):
    return requests.delete(url=f"{url}/{note_id}", headers=headers)


url = 'http://localhost:8000/notes'

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbnNodWdhcmciLCJleHAiOjE3MTE2Mzk5ODB9.ZBfDJkU_-m7oDl0G4TeNT6pc_Twc4mzLAim81MU1pmc"

headers = {
    'Authorization': f'Bearer {token}'
}

json = {
    "title": "Python",
    "content": "Python is a high-level, general-purpose programming language."
}

response = test_create_note(url, headers, json)
print(f"\nRESPONSE :: {response.json()}\n")

note_id = "660586ec2817881f19ce97c0"

response = test_get_note_by_id(url, headers, note_id)
print(f"\nRESPONSE :: {response.json()}\n")

response = test_get_notes(url, headers)
print(f"\nRESPONSE :: {response.json()}\n")

json = {
    "title": "FastAPI",
    "content": "FastAPI is a modern web framework first released in 2018 for building RESTful APIs in Python."
}

response = test_update_note_by_id(url, headers, note_id, json)
print(f"\nRESPONSE :: {response.json()}\n")

response = test_delete_note_by_id(url, headers, note_id)
print(f"\nRESPONSE :: {response.json()}\n")
