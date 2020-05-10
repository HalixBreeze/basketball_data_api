from flask import Flask
import db_processor
import json

APP = Flask('__name__')

def get_json_data(data, titles):
    json_data = []
    for row in data:
        if len(row) != len(titles):
            print('The amount of field is false!!')
            return []
            
        one_record = dict()
        for i in range(0, len(titles)):
            title = titles[i]
            field = row[i]
            one_record[title] = field
        json_data.append(one_record)
    return json_data

@APP.route('/')
def index():
    return 'Home Page'

@APP.route('/seasons')
def get_seasons():
    sql = 'SELECT * FROM `season`'
    seasons = db_processor.get_data(sql)

    titles = ['id', 'year', 'name']
    data = get_json_data(seasons, titles)

    return json.dumps(data)

@APP.route('/teams')
def get_teams():
    sql = 'SELECT * FROM `team`'
    teams = db_processor.get_data(sql)

    titles = ['id', 'name']
    data = get_json_data(teams, titles)

    return json.dumps(data)

@APP.route('/players')
def get_players():
    sql = 'SELECT * FROM `player`'
    players = db_processor.get_data(sql)
    
    titles = ['id', 'name', 'age', 'jersey', 'height', 'weight', 'position', 'team_id']
    data = get_json_data(players, titles)

    return json.dumps(data)

@APP.route('/games')
def get_games():
    sql = 'SELECT * FROM `game`'
    games = db_processor.get_data(sql)

    titles = ['id', 'start_time', 'win_team_id', 'lose_team_id', 'win_team_score', 'lose_team_score', 'season_id']
    data = get_json_data(games, titles)

    return json.dumps(data)

@APP.route('/game-player-records')
def get_game_player_records():
    sql = 'SELECT * FROM `game_player_record`'
    records = db_processor.get_data(sql)

    titles = ['id', 'playing_time', 'two_PT_all', 'two_PT_success', 'three_PT_all', 'three_PT_success', 'free_throw_all', 'free_throw_success', 'turnover', 'foul', 'steal', 'rebound', 'assist', 'block', 'game_id', 'player_id']
    data = get_json_data(records, titles)

    return json.dumps(data)

if __name__ == '__main__':
    APP.debug = True
    APP.run()