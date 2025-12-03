# Console Casino System

## Project Overview
This is a simple console-based casino application written in Python using SQLite3 for data persistence. The app supports user registration, sign-in (via username or email), profile management, depositing money, and playing casino games (baccarat, blackjack, slots). It displays real-time balance updates during gameplay and saves data locally with SQLite.

This project is barebones and designed for learning and experimentation with Python console apps and basic database integration.

## Project Structure

```
casino_console/
│
├── data/ # SQLite database file stored here (created at runtime)
│ └── casino.db
├── src/ # Source code folder
│ ├── main.py # Main app entry and CLI loop
│ ├── db.py # SQLite connection, schema init, CRUD helper functions
│ ├── auth.py # User registration and authentication logic
│ ├── profile.py # Profile update, delete operations
│ ├── wallet.py # Deposit and balance management
│ ├── ui.py # Console input/output helpers and validation
│ ├── models.py # User and session data models
│ ├── state.py # In-memory session state (current user)
│ └── games/ # Game implementations
│ ├── init.py
│ ├── baccarat.py
│ ├── blackjack.py
│ ├── slots.py
│ └── common.py # Shared game utilities (bet, balance updates)
├── tests/ # Optional test scripts
│
├── README.md # This file
├── requirements.txt # Python dependencies (can be empty as stdlib used)
└── .gitignore # Ignore typical Python and SQLite files
```


## How to Run
1. Make sure you have Python 3.10+ installed.  
2. Clone/download the repo.  
3. (Optional) Create a virtual environment and activate it:  

```
python -m venv .venv
source .venv/bin/activate # Unix/macOS
..venv\Scripts\activate # Windows
```

4. Run the main app:  

```python -m src.main```

5. The app will create the SQLite database file (`casino.db`) in the `data/` folder if it doesn't exist on startup.

## How to Contribute
- Fork the repository.  
- Create a new branch for your feature or bug fix.  
- Write clear, concise code with comments where necessary.  
- Test your changes locally (optional tests can be in `tests/`).  
- Commit your changes following clear commit messages.  
- Submit a pull request describing your changes and motivation.

## Important Notes
- The app stores balance in the database as integer cents to avoid floating point money issues.
- Input validation is basic; expect minimal error handling suitable for CLI usage.
- No advanced design patterns or frameworks used; code is straightforward procedural/functional style.
- Feel free to extend with more games or polishing UI as learning exercises.