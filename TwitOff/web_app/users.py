import sqlite3
import os

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "twitoff_development.db")

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

user_query = '''
            SELECT screen_name
            FROM user; 
            '''

user_results = cursor.execute(user_query).fetchall()

user_list = []

punctuation = ["(",")","'"]

for user in user_results:
    user = user[0]
    user_list.append(user)


print(user_list)