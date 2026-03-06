import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"   # website to scrape

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# find all news titles
titles = soup.find_all("span", class_="titleline")

for i, title in enumerate(titles, start=1):
    print(i, title.text)