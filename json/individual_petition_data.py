import requests


url = 'https://petition.parliament.uk/petitions/569957'

def getJson(url):
    json_url = url + '.json'

    response = requests.get(json_url).json()

    return response


def signaturesByConstituency(json):
    return json['data']['attributes']['signatures_by_constituency']



json_data = getJson(url)
print(signaturesByConstituency(json_data))
