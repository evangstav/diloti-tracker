from .conftest import client


# In test_teams.py
def test_create_team():
    team_data = {
        "name": "Test Team",
        "player1_name": "Test Player 1",
        "player2_name": "Test Player 2",
    }
    response = client.post("/teams/", json=team_data)
    assert response.status_code == 200
    assert response.json()["name"] == team_data["name"]


def test_read_teams():
    response = client.get("/teams/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
