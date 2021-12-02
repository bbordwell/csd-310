#Ben Bordwell Moudle 9.3 assignment 12/1/2021
#This program inserts a new player, updates it, then deletes it.

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


#Insert new player.
cursor.execute("""INSERT INTO player (first_name, last_name, team_id)
                VALUES('Alatar', 'The Blue', 1);""")


#Show the players table which should include the previously added player.
cursor.execute("""SELECT player_id, first_name, last_name, team_name
                FROM player
                INNER JOIN team
                    ON player.team_id = team.team_id;""")
players = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER INSERT --")
for row in players:
    print(f"Player ID: {row[0]}")
    print(f"First Name: {row[1]}")
    print(f"Last Name: {row[2]}")
    print(f"Team Name: {row[3]}")
    print()


#Change the team of the new player.
cursor.execute("""UPDATE player
                SET team_id = 2
                WHERE first_name = 'Alatar';""")


#Show the players after the update.
cursor.execute("""SELECT player_id, first_name, last_name, team_name
                FROM player
                INNER JOIN team
                    ON player.team_id = team.team_id;""")
players = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER UPDATE --")
for row in players:
    print(f"Player ID: {row[0]}")
    print(f"First Name: {row[1]}")
    print(f"Last Name: {row[2]}")
    print(f"Team Name: {row[3]}")
    print()


#Delete the new player.
cursor.execute("""DELETE FROM player
                WHERE first_name = 'Alatar';""")


#Show the players after the deletion.
cursor.execute("""SELECT player_id, first_name, last_name, team_name
                FROM player
                INNER JOIN team
                    ON player.team_id = team.team_id;""")
players = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER DELETE --")
for row in players:
    print(f"Player ID: {row[0]}")
    print(f"First Name: {row[1]}")
    print(f"Last Name: {row[2]}")
    print(f"Team Name: {row[3]}")
    print()