import streamlit as st
import requests

# API_BASE_URL = "http://localhost:8000"
API_BASE_URL = "https://diloti-tracker.herokuapp.com:8000"

# response = requests.get("https://diloti-tracker-backend.herokuapp.com/games/")
# print(response.json())


def fetch_teams():
    response = requests.get(f"{API_BASE_URL}/teams/")
    return response.json()


def fetch_players():
    response = requests.get(f"{API_BASE_URL}/players/")
    return response.json()


def fetch_games():
    response = requests.get(f"{API_BASE_URL}/games/")
    return response.json()


def create_team(team):
    response = requests.post(f"{API_BASE_URL}/teams/", json=team)
    return response.json()


def create_game(game):
    response = requests.post(f"{API_BASE_URL}/games/", json=game)
    return response.json()


st.title("Diloti Tracker")

st.header("Teams")
teams = fetch_teams()
# for team in teams:
#     st.write(team["name"])

st.header("Create Team")
team_name = st.text_input("Team Name")
player1_name = st.text_input("Player 1 Name")
player2_name = st.text_input("Player 2 Name")

if st.button("Create Team"):
    team = {
        "name": team_name,
        "player1_name": player1_name,
        "player2_name": player2_name,
    }
    created_team = create_team(team)
    st.write(f"Created team {created_team['name']}")

st.header("Games")
games = fetch_games()
for game in games:
    st.write(
        f"{game['team1_name']} {game['team1_score']} - {game['team2_name']} {game['team2_score']}"
    )

st.header("Create Game")
team1_name = st.selectbox("Team 1", [team["name"] for team in teams])
team2_name = st.selectbox("Team 2", [team["name"] for team in teams], index=1)
team1_score = st.number_input("Team 1 Score", min_value=0, step=1)
team2_score = st.number_input("Team 2 Score", min_value=0, step=1)
if st.button("Create Game"):
    game = {
        "team1_name": team1_name,
        "team2_name": team2_name,
        "team1_score": team1_score,
        "team2_score": team2_score,
    }
    created_game = create_game(game)
    st.write(
        f"Created game {created_game['team1_name']} {created_game['team1_score']} - {created_game['team2_name']} {created_game['team2_score']}"
    )
