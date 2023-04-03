# Diloti Tracker API

This repository contains the source code for the Diloti Tracker API, a FastAPI-based application designed to store and manage game scores, teams, and players for the card game Diloti. The API is built using FastAPI, SQLite, and SQLAlchemy.

## Features

- CRUD operations for games, teams, and players in Diloti
- Automatic player creation when creating a team
- Check for duplicate team names
- Query players by name
- Pre-commit hooks with Black code formatter, ruff linting, and other useful checks

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- Pre-commit (optional, for development purposes)

## Installation

1. Clone the repository:

``` bash
git clone https://github.com/yourusername/diloti-tracker.git
```

2. Change to the repository directory:

``` bash
cd diloti-tracker
```

3. Create a virtual environment and activate it:

``` bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required packages:

``` bash
pip install -r requirements.txt
```

5. (Optional) Install pre-commit hooks for development purposes:

``` bash
pip install pre-commit
pre-commit install
```


## Running the API

To start the API server, run the following command:

``` bash
uvicorn app.main:app --reload
```


The API will be available at http://localhost:8000, and you can view the interactive API documentation at http://localhost:8000/docs.

## Usage

The API will provide the following endpoints:

- `/games/` - Create and read games
- `/games/{game_id}` - Read, update, and delete a game by ID
- `/teams/` - Create and read teams
- `/teams/{team_id}` - Read, update, and delete a team by ID
- `/players/` - Create and read players
- `/players/{player_id}` - Read, update, and delete a player by ID
- `/players/by_name/{player_name}` - Read a player by name

Use the interactive API documentation at http://localhost:8000/docs to explore the available endpoints and their parameters.

## Contributing

Contributions are welcome! Please feel free to submit issues for bug reports, feature requests, or improvements. If you'd like to contribute code, please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
