import csv

def scrapeArrayToJson(data):
    data = data
    json = {'petitions': {'source': 'petitions.parliament.uk', 'list': []}}

    for petition in data:
        json['petitions']['list'].append({
            'Constituency': petition[0],
            'Area': petition[1],
            'Web Link': petition[2],
            'MP': petition[3],
            'P1N': petition[4],
            'P1LS': petition[5],
            'P1NS': petition[6],
            'P2N': petition[7],
            'P2LS': petition[8],
            'P2NS': petition[9],
            'P3N': petition[10],
            'P3LS': petition[11],
            'P3NS': petition[12]
        })

    return json


def writeToCSV(data, file):
    rows = data['petitions']['list']

    with open(file, mode='w') as csv_file:
        fieldnames = [
                      'Constituency',
                      'Area',
                      'Web Link',
                      'MP',
                      'P1N',
                      'P1LS',
                      'P1NS',
                      'P2N',
                      'P2LS',
                      'P2NS',
                      'P3N',
                      'P3LS',
                      'P3NS'
                      ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            writer.writerow({
                      'Constituency': row['Constituency'],
                      'Area': row['Area'],
                      'Web Link': row['Web Link'],
                      'MP': row['MP'],
                      'P1N': row['P1N'],
                      'P1LS': row['P1LS'],
                      'P1NS': row['P1NS'],
                      'P2N': row['P2N'],
                      'P2LS': row['P2LS'],
                      'P2NS': row['P2NS'],
                      'P3N': row['P3N'],
                      'P3LS': row['P3LS'],
                      'P3NS': row['P3NS']
                      })

    print("Finished writing to CSV.")
