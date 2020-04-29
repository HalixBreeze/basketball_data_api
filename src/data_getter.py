from  requests_html import HTMLSession
import json

def get_game(url):
    pass

if __name__ == '__main__':
    session = HTMLSession()
    url = 'https://choxue.com/api/v1/v7/legacy/v2/seasons/WJC40_FEMALE_jYGbCAfRc/teams'
    response = session.get(url)
    html = response.html

    teams = json.loads(html.html)

    for team in teams:
        print(team.keys())
        print(team.values())