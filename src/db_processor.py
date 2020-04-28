import sqlite3

def create_jones_cup_db():
    print('Creating Database...')

    connection = sqlite3.connect('jones_cup_db')
    cursor = connection.cursor()

    sql = 'CREATE TABLE IF NOT EXISTS game (\
        id INTEGER PRIMARY KEY IS NOT NULL,\
        start_time,\
        win_team_id,\
        lose_team_id,\
        win_team_score,\
        lose_team_score,\
        season_id\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS player (\
        id,\
        name,\
        height,\
        weight,\
        position,\
        two_point,\
        three_point,\
        rebound,\
        team_id\
        )'
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS season (\
        id,\
        year,\
        name,\
    )
    '
    cursor.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS team (\
        id,\
        name\
    )
    '
    cursor.execute(sql)

    connection.commit()
    connection.close()

if __name__ == '__main__':