import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import re
import csv
from constituency import Constituency

def getAllConstituencyNames():
    print("Getting constituency web addresses")
    