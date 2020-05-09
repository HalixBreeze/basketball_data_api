import db_processor

def add_team():
    name = input('輸入欲新增的隊伍名稱︰')

    sql = f"INSERT INTO team (`name`) VALUES ('{name}')"
    db_processor.change_data(sql)

    print(f'<{name}>已新增')

def add_player():
    common_text = '輸入欲新增球員的'

    name = input(f'{common_text}名字︰')
    age = input(f'{common_text}年齡︰')
    jersey = input(f'{common_text}背號︰')
    height = input(f'{common_text}身高︰')
    weight = input(f'{common_text}體重︰')
    position = input(f'{common_text}位置︰')
    team = input(f'{common_text}所屬球隊︰')

    sql = f"SELECT `id` FROM `team` WHERE name = '{team}'"
    team_id = db_processor.get_data(sql)[0][0]

    sql = f"INSERT INTO player (`name`, `age`, `jersey`, `height`, `weight`, `position`, `team_id`)\
        VALUES ('{name}', {age}, {jersey}, {height}, {weight}, '{position}', {team_id})"
    db_processor.change_data(sql)

    print(f'<{name}>已新增')

def add_season():
    common_text = '輸入該賽季的'

    year = input(f'{common_text}年份：')
    name = input(f'{common_text}名稱：')

    sql = f"INSERT INTO season (`year`, `name`)\
        VALUES ({year}, '{name}')"
    db_processor.change_data(sql)

    print(f'{name}已新增')

def add_game():
    common_text = '輸入該比賽的'

    season = input(f'{common_text}賽季名稱：')
    sql = f"SELECT `id` FROM `season` WHERE `name` = '{season}'"
    season_id = db_processor.get_data(sql)[0][0]

    date = input(f'{common_text}比賽日期（EX：2020-01-01）：')
    time = input(f'{common_text}比賽時間（EX：15:00）：')
    start_time = date + ' ' + time

    win_team = input(f'{common_text}勝利隊伍：')
    sql = f"SELECT `id` FROM `team` WHERE `name` = '{win_team}'"
    win_team_id = db_processor.get_data(sql)[0][0]

    win_team_score = input(f'{common_text}勝利隊伍得分：')

    lose_team = input(f'{common_text}落敗隊伍：')
    sql = f"SELECT `id` FROM `team` WHERE `name` = '{lose_team}'"
    lose_team_id = db_processor.get_data(sql)[0][0]

    lose_team_score = input(f'{common_text}落敗隊伍得分：')

    sql = f"INSERT INTO game (`start_time`, `win_team_id`, `lose_team_id`, `win_team_score`, `lose_team_score`, `season_id`)\
        VALUES ('{start_time}', {win_team_id}, {lose_team_id}, {win_team_score}, {lose_team_score}, {season_id})"
    db_processor.change_data(sql)

    print('比賽紀錄已新增')

def add_game_player_record():
    print('---請輸入單場比賽中，個別球員的比賽數據---')
    
    date = input('輸入比賽日期（EX：2020-01-01）：')
    time = input('輸入比賽時間（EX：15:00）：')
    date_time = date + ' ' + time

    team = input('輸入選手所屬隊伍：')
    sql = f"SELECT `id` FROM `team` WHERE `name` = '{team}'"
    team_id = db_processor.get_data(sql)[0][0]

    sql = f"SELECT `id`\
        FROM `game`\
        WHERE `start_time` = '{date_time}'\
            AND (`win_team_id` = {team_id}\
                OR `lose_team_id` = {team_id})"
    game_id = db_processor.get_data(sql)[0][0]

    player = input('輸入選手姓名：')
    sql = f"SELECT `id` FROM `player` WHERE `name` = '{player}' AND `team_id` = {team_id}"
    player_id = db_processor.get_data(sql)[0][0]

    playing_time = input('輸入選手的上場時間（分鐘）：')
    two_PT_all = input('輸入選手的2分球出手次數：')
    two_PT_success = input('輸入選手的2分球得分次數：')
    three_PT_all = input('輸入選手的3分球出手次數：')
    three_PT_success = input('輸入選手的3分球得分次數：')
    free_throw_all = input('輸入選手的罰球次數：')
    free_throw_success = input('輸入選手的罰球得分次數：')
    turnover = input('輸入選手的失誤次數：')
    foul = input('輸入選手的犯規次數：')
    steal = input('輸入選手的抄截數：')
    rebound = input('輸入選手的籃板數：')
    assist = input('輸入選手的助攻數：')
    block = input('輸入選手的阻攻數：')

    sql = f"INSERT INTO `game_player_record` (`playing_time`, `two_PT_all`, `two_PT_success`, `three_PT_all`, `three_PT_success`,  `free_throw_all`, `free_throw_success`, `turnover`, `foul`, `steal`,  `rebound`, `assist`, `block`, `game_id`, `player_id`)\
        VALUES ({playing_time}, {two_PT_all}, {two_PT_success}, {three_PT_all}, {three_PT_success}, {free_throw_all}, {free_throw_success}, {turnover}, {foul}, {steal}, {rebound}, {assist}, {block}, {game_id}, {player_id})"
    db_processor.change_data(sql)

if __name__ == '__main__':
    add_game_player_record()