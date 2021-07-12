import requests
from bs4 import BeautifulSoup

URL = "https://www.hltv.org/matches"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

mydivs = soup.find_all("div", {"class": "upcomingMatchesSection"})
print(mydivs)