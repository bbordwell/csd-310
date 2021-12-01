#Ben Bordwell Moudle 9.2 assignment 12/1/2021
#This program uses an inner join to display names and respective teams.

import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'pysports_user',
    'password' : 'MySQL8IsGreat!',
    'host': '127.0.0.1',
    'database': 'pysports',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

cursor.execute("""SELECT player_id, first_name, last_name, team_name
                FROM player
                INNER JOIN team
                    ON player.team_id = team.team_id;""")
players = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --")
for row in players:
    print(f"Player ID: {row[0]}")
    print(f"First Name: {row[1]}")
    print(f"Last Name: {row[2]}")
    print(f"Team Name: {row[3]}")
    print()