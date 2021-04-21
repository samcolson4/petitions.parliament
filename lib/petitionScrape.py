from allurls import allConstituencies
from writer import scrapeArrayToJson
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import re


#  get MP name
#  get top three petitions & numbers for them 
#  write to CSV in correct constituency

def getMPName(soup):
    if soup.find(class_="lede"):
        return soup.find(class_="lede").find('a').text
    else:
        return ""


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
    all_data = []

    for constituency in constits:
        constituency_data = []
        page = requests.get(constituency.link)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        mp_name = getMPName(soup)

        petition_data = getPetitionData(soup)

        constituency_data.append(constituency.constituency)
        constituency_data.append(constituency.area)
        constituency_data.append(constituency.link)
        constituency_data.append(mp_name)
        constituency_data.extend(petition_data)

        print(constituency_data)
        print("\n")
        all_data.append(constituency_data)
    
    return all_data


def runScript():
    # 1. Get data         
    data = getData()

    # 2. Write data to CSV
    json = scrapeArrayToJson(data)
    print(json)

    file = './constituency_output.csv'