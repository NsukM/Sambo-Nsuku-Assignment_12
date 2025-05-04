from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_summary_report():
    response = client.get("/api/reports/summary")
    assert response.status_code == 200
    assert "total_users" in response.json()


