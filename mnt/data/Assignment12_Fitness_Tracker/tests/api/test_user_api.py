from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_user():
    response = client.post("/api/users", params={
        "user_id": "2", "name": "Sam", "email": "sam@mail.com", "password": "1234", "goal": "Gain muscle"
    })
    assert response.status_code == 200
    get_response = client.get("/api/users/2")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Sam"



