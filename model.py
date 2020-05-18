import json


def db_function():
    with open('db.json') as f:
        return json.load(f)


def save_db():
    with open('db.json', 'w') as f:
        return json.dump(db, f)


db = db_function()
