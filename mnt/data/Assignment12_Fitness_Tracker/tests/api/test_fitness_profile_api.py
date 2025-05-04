from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_and_get_profile():
    response = client.post("/api/profiles", params={
        "age": 30, "weight": 80.0, "height": 180.0, "activity_level": "Moderate"
    })
    assert response.status_code == 200
    get_response = client.get("/api/profiles/30")
    assert get_response.status_code == 200
    assert get_response.json()["activity_level"] == "Moderate"


