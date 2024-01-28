import requests
from bs4 import BeautifulSoup

URL = "https://www.timeanddate.com/weather/ukraine/kyiv/historic?hd=20240121"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("table", id="wt-his")
tds = table.find_all("td")

for localTd in tds:
	print(localTd.text)

