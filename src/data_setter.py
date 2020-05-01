import db_processor


def add_team():
    name = input('輸入欲新增的隊伍名稱︰')

    db_path = r'../db/jones_cup_db.sqlite'
    sql = f"INSERT INTO team (`name`) VALUES ('{name}')"
    db_processor.change_data(db_path, sql)

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

    print(f'<{name}>已新增')

if __name__ == '__main__':
    add_team()