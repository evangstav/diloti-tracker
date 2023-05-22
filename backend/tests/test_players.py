from .conftest import client


def test_create_player():
    player_data = {"name": "Test Player"}
    response = client.post("/players/", json=player_data)
    assert response.status_code == 200
    assert response.json()["name"] == player_data["name"]


def test_read_players():
    response = client.get("/players/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_player():
    response = client.get("/players/")
    player_name = response.json()[0]["name"]

    response = client.get(f"/players/{player_name}")
    assert response.status_code == 200
    assert response.json()["name"] == player_name
