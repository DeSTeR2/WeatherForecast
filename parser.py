import requests
from bs4 import BeautifulSoup
import selenium
#from lxml import html

class Parser:
    _baseLink = "https://www.timeanddate.com/weather"
    _historic = "/historic"
    _dMonth = "?month="
    _dYear = "&year="


    _link = ""
    def __init__(self, country, sity):
        self._link = self._baseLink + "/" + country + "/" + sity + self._historic

    def __getAllLinks(self, soup):
        links = []

        for year in range(2020,2024):
            for mounth in range(1,12):
                addLink = self._link + self._dMonth + str(mounth) + self._dYear + str(year)
                links.append(addLink)
        return links


    def __getWeatherLinks(self, soup):
        soup = soup.select('div:nth-of-type(5) > main > article > div:nth-of-type(6) > div:nth-of-type(3)')
        soup[0].select('a[href]')

        hrefs = []
        for href in soup[0].select('a[href]'):
            text = str(href['href'])
            text = text.replace('/weather', '')
            hrefs.append(text)

        return hrefs

    def __parseWeather(self, link):

        print("Parsing date: " + link[len(link)-8:len(link)-4] + "/" + link[len(link)-4:len(link)-2] + "/" + link[len(link)-2:len(link)] )

        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.find("table", id="wt-his")
        tds = table.find_all("td")

        #print(table)

        for localTd in tds:
            if localTd.text == "No data available for the given date. Try selecting a different day.":
                break
            print(localTd.text)

    def __linkProcces(self, link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        hrefs = self.__getWeatherLinks(soup)

        for href in hrefs:
            self.__parseWeather(self._baseLink + href)
    def parse(self):
        page = requests.get(self._link)
        soup = BeautifulSoup(page.content, "html.parser")


        links = self.__getAllLinks(soup)

        #print(links[0])

        for link in links:
            print("Processing link: " + link)
            self.__linkProcces(link)
