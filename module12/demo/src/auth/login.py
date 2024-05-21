from src.db_client.sql_client import SQLClient
from src.config import DB_NAME, USER_NAME, USER_PASSWORD

def login_user(email, password):
    client = SQLClient(DB_NAME, USER_NAME, USER_PASSWORD)

    if client.read(email) is not None:
        print("Welcome")
    else:
        print("Refresh the page and give error message")