import requests

ENDPOINT = "http://localhost:4000/movies"

response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)

status_code = response.status_code
print(status_code)

def test_index():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    

