import json
from pathlib import Path

db_file = Path("balance.json")

def load_data():
    if db_file.exists():
        with db_file.open("r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with db_file.open("w") as f:
        json.dump(data, f)

def get_balance(user_id):
    data = load_data()
    return data.get(user_id, 0)

def update_balance(user_id, amount):
    data = load_data()
    data[user_id] = data.get(user_id, 0) + amount
    save_data(data)
