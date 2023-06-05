# Chat API using WebSocket Protocol

## Features
1) CRUD operations for user, message, and chat entities.
2) Creating chat rooms for 2 or more participants.
3) Authentication using JWT token.
## Installation
1) Install dependencies: pip install -r requirements.txt
2)  Create a .env file and fill it out following the example in example.env.
3) Create the database using migrations: `alembic upgrade head`
4) Start the server: `python3 main.py`
5) Access the Swagger documentation at `host:port/docs` to view the API documentation.