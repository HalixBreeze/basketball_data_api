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
        start_time TEXT NOT NULL,\
        win_team_id TEXT NOT NULL,\
        lose_team_id TEXT NOT NULL,\
        win_team_score INTEGER,\
        lose_team_score INTEGER,\
        season_id TEXT NOT NULL,\
        UNIQUE(season_id, start_time, win_team_id)\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS player (\
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        name TEXT NOT NULL,\
        age INTEGER,\
        jersey INTEGER,\
        height INTEGER,\
        weight INGEGER,\
        position TEXT,\
        team_id TEXT NOT NULL,\
        UNIQUE(team_id, name)\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS game_player_record (\
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        playing_time INTEGER,\
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
        block INTEGER,\
        game_id TEXT NOT NULL,\
        player_id TEXT NOT NULL,\
        UNIQUE(game_id, player_id)\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS season (\
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        year INTEGER NOT NULL,\
        name TEXT NOT NULL,\
        UNIQUE(name)\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS team (\
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        name TEXT NOT NULL,\
        UNIQUE(name)\
        )'
    cursor.execute(sql)

    connection.commit()
    connection.close()
    print('Created Database Completely!!')

def change_data(db_path, sql):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(sql)
    connection.commit()
    connection.close()

def get_data(db_path, sql):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(sql)
    result = cursor.fetchall()
    connection.close()

    return result

if __name__ == '__main__':
    sql = "select * from team"
    data = get_data(r'../db/jones_cup_db.sqlite', sql)
    print(data)