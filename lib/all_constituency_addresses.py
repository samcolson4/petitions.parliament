import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
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
          print(row[0])
          constituencies.append(Constituency(row[0], row[1], row[2]))
    
    return constituencies

list = importConstituencies()
print(len(list))
