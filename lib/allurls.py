import requests
from bs4 import BeautifulSoup
import requests
import re
import csv
from constituency import Constituency


def importConstituencies():
  constituencies = []

  with open('constituencies.csv', mode='r') as f:
    reader = csv.reader(f)

    for row in reader:
      if row[0] == 'Constituency':
        continue
      else: 
        # print(row[0])
        constituencies.append(Constituency(row[0], row[1], row[2]))
  
  return constituencies


def getURLS(constituencies):
  base_url = 'https://petition.parliament.uk/petitions/local/'

  for constituency in constituencies:
    # print("\nChecking constituency name")
    add_url = constituency.constituency.replace(" ", "-").replace(",", "")
    full_url = base_url + add_url.lower()
    constituency.link = full_url
    # print(constituency.constituency)
    # print(constituency.link)
  
  return constituencies


def checkBrokenPages(url_list):
    broken = []

    for const in url_list:
      url = const.link
      page = requests.get(url)
      soup = BeautifulSoup(page.content, 'html.parser')

      if "The page you're looking for doesn't exist" in soup.find('h1').text:
        broken.append(const.constituency)
        print(url)
      else:
        continue
    
    print(broken)


def allConstituencies():
    list = importConstituencies()
    constituencies = getURLS(list)

    return constituencies
