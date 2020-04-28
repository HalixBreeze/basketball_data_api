import os
import sqlite3

def create_jones_cup_db():
    print('Creating Database...')

    if os.path.isdir(r'../db') != True:
        os.mkdir(r'../db')

    connection = sqlite3.connect(r'../db/jones_cup_db.sqlite')
    cursor = connection.cursor()

    sql = 'CREATE TABLE IF NOT EXISTS game (\
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        start_time TEXT,\
        win_team_id INTEGER,\
        lose_team_id INTEGER,\
        win_team_score INTEGER,\
        lose_team_score INTEGER,\
        season_id INTEGER\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS player (\
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        name TEXT NOT NULL,\
        age INTEGER,\
        jersey INTEGER,\
        height INTEGER,\
        weight INGEGER,\
        position TEXT\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS game_player_record (\
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        game_id INTEGER NOT NULL,\
        player_id INTEGER NOT NULL,\
        play_time INTEGER,\
        two_PT_all INTEGER,\
        two_PT_success INTEGER,\
        three_PT_all INTEGER,\
        threethree_PT_success INTEGER,\
        free_throw INTEGER,\
        turnover INTEGER,\
        foul INTEGER,\
        steal INTEGER,\
        rebound INTEGER,\
        assist INTEGER,\
        block INTEGER\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS season (\
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        year INTEGER NOT NULL,\
        name TEXT NOT NULL\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS team (\
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        name TEXT NOT NULL\
        )'
    cursor.execute(sql)

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_jones_cup_db()