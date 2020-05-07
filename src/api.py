from flask import Flask
import db_processor
import json

APP = Flask('__name__')
DB_PATH = r'../db/jones_cup_db.sqlite'

@APP.route('/')
def index():
    return 'Home Page'

@APP.route('/seasons')
def get_seasons():
    sql = 'SELECT * FROM `season`'
    seasons = db_processor.get_data(DB_PATH, sql)
    seasons = json.dumps(seasons)

    return seasons

@APP.route('/teams')
def get_teams():
    sql = 'SELECT * FROM `team`'
    teams = db_processor.get_data(DB_PATH, sql)
    teams = json.dumps(teams)

    return teams

@APP.route('/players')
def get_players():
    sql = 'SELECT * FROM `player`'
    players = db_processor.get_data(DB_PATH, sql)
    players = json.dumps(players)

    return players

@APP.route('/games')
def get_games():
    sql = 'SELECT * FROM `game`'
    games = db_processor.get_data(DB_PATH, sql)
    games = json.dumps(games)

    return games

@APP.route('/game-player-records')
def get_game_player_records():
    sql = 'SELECT * FROM `game_player_record`'
    records = db_processor.get_data(DB_PATH, sql)
    records = json.dumps(records)

    return records

if __name__ == '__main__':
    APP.debug = True
    APP.run()