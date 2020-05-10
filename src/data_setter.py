import db_processor

def add_team(name):
    sql = f"INSERT INTO team (`name`) VALUES ('{name}')"
    db_processor.change_data(sql)

    print(f'<{name}>已新增')

def add_player(name, age, jersey, height, weight, position, team_id):
    sql = f"INSERT INTO player (`name`, `age`, `jersey`, `height`, `weight`, `position`, `team_id`)\
        VALUES ('{name}', {age}, {jersey}, {height}, {weight}, '{position}', {team_id})"
    db_processor.change_data(sql)

    print(f'<{name}>已新增')

def add_season(year, name):
    sql = f"INSERT INTO season (`year`, `name`)\
        VALUES ({year}, '{name}')"
    db_processor.change_data(sql)

    print(f'{name}已新增')

def add_game(season_id, start_time, win_team_id, lose_team_id, win_team_score, lose_team_score):
    sql = f"INSERT INTO game (`start_time`, `win_team_id`, `lose_team_id`, `win_team_score`, `lose_team_score`, `season_id`)\
        VALUES ('{start_time}', {win_team_id}, {lose_team_id}, {win_team_score}, {lose_team_score}, {season_id})"
    db_processor.change_data(sql)

    print('比賽紀錄已新增')

def add_game_player_record(game_id, player_id, playing_time, two_PT_all, two_PT_success, three_PT_all, three_PT_success, free_throw_all, free_throw_success, turnover, foul, steal, rebound, assist, block):
    sql = f"INSERT INTO `game_player_record` (`playing_time`, `two_PT_all`, `two_PT_success`, `three_PT_all`, `three_PT_success`,  `free_throw_all`, `free_throw_success`, `turnover`, `foul`, `steal`,  `rebound`, `assist`, `block`, `game_id`, `player_id`)\
        VALUES ({playing_time}, {two_PT_all}, {two_PT_success}, {three_PT_all}, {three_PT_success}, {free_throw_all}, {free_throw_success}, {turnover}, {foul}, {steal}, {rebound}, {assist}, {block}, {game_id}, {player_id})"
    db_processor.change_data(sql)

if __name__ == '__main__':
    add_game_player_record()