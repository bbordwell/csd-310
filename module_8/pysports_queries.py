#Ben Bordwell Module 8.3 assignment 11/24/2021
#This program queries pysports for the teams and players.

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

cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()
print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print(f"Team ID: {team[0]}")
    print(f"Team Name: {team[1]}")
    print(f"Mascot: {team[2]}")
    print()
print()

print("-- DISPLAYING PLAYER RECORDS --")
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team ID: {player[3]}")
    print()