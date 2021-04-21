from allurls import allConstituencies
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import re


#  get MP name
#  get top three petitions & numbers for them 
#  write to CSV in correct constituency

def getMPName(soup):
    return soup.find(class_="lede").find('a').text


def getSigs(item):
    full_string = item.find('p').text
    split_text = full_string.split("(")
    output_text = []
    
    for text in split_text:
        digits = re.sub('\D', '', f'{text}')
        output_text.append(digits)

    return output_text[0], output_text[1]


def getPetitionData(soup):
    petition_data = []
    
    petitions = soup.find_all(class_="petition-item")
    only_three = [petitions[0], petitions[1], petitions[2]]

    for petition_item in only_three:
        pn = petition_item.find('h2').text
        pls, pns = getSigs(petition_item)

        petition_data.extend([pn, pls, pns])
    
    return petition_data


def getData():
    constits = allConstituencies()

    for constituency in constits:
        page = requests.get(constituency.link)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        mp_name = getMPName(soup)

        petition_data = getPetitionData(soup)

        print(constituency.constituency, mp_name, petition_data)
        print("\n")

        

getData()