import requests

API_BASE_URL = "http://localhost:8000"

players_data = [
    {"name": "Alice"},
    {"name": "Bob"},
    {"name": "Charlie"},
    {"name": "David"},
]

# Create teams and their players
team_data = [
    {
        "name": "Team A",
        "player1_name": "Alice",
        "player2_name": "Bob",
    },
    {
        "name": "Team B",
        "player1_name": "Charlie",
        "player2_name": "David",
    },
]

team_ids = []
for data in team_data:
    response = requests.post(f"{API_BASE_URL}/teams/", json=data)
    team = response.json()
    print(f"Created team: {team}")
    # team_ids.append(team["id"])

game_data = [
    {
        "team1_name": "Team A",
        "team2_name": "Team B",
        "team1_score": 15,
        "team2_score": 0,
        "timestamp": "2023-05-02",
    },
    {
        "team1_name": "Team A",
        "team2_name": "Team B",
        "team1_score": 0,
        "team2_score": 15,
        "timestamp": "2023-05-03",
    },
]

for data in game_data:
    response = requests.post(f"{API_BASE_URL}/games/", json=data)
    game = response.json()
    print(f"Created game: {game}")
