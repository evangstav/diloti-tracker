from datetime import date
from .conftest import client


def test_create_game():
    team1_data = {
        "name": "Test Team 1",
        "player1_name": "Test Player 1",
        "player2_name": "Test Player 2",
    }
    team2_data = {
        "name": "Test Team 2",
        "player1_name": "Test Player 3",
        "player2_name": "Test Player 4",
    }
    response1 = client.post("/teams/", json=team1_data)
    response2 = client.post("/teams/", json=team2_data)
    team1_name = response1.json()["name"]
    team2_name = response2.json()["name"]

    game_data = {
        "team1_name": team1_name,
        "team2_name": team2_name,
        "team1_score": 10,
        "team2_score": 20,
        "date": date.today().isoformat(),
    }
    response = client.post("/games/", json=game_data)
    assert response.status_code == 200
    assert response.json()["team1_score"] == game_data["team1_score"]
    assert response.json()["team2_score"] == game_data["team2_score"]


def test_read_games():
    response = client.get("/games/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
