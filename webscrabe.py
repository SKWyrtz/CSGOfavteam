import requests
from bs4 import BeautifulSoup

URL = "https://www.hltv.org/ranking/teams"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
team_names = []

def get_top30_team_names():
    teams_DIVs = soup.find_all("div", {"class": "ranked-team standard-box"})
    for div in teams_DIVs:
        name = div.find("span", class_="name")
        team_names.append(name.text.strip())
    return team_names