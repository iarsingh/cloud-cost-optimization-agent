from fastapi.testclient import TestClient
from costagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'find expensive services', **{'payload': {'lines': [{'service': 'gke', 'cost': 80}, {'service': 'dns', 'cost': 2}]}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["flags"] == ["gke"]
    refused = client.post("/agent/run", json={"goal": 'resize the cluster now'}).json()
    assert refused["refused"] is True
