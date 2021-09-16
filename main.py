import requests
import json

data = requests.get("https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=09fc3b3c9df37bf824f90d470a4f")
data_set = data.json()

if data.status_code == 404:
    with open('dataset.json') as file:
        data_set = json.load(file)

new_dict = {}
for key in data_set['events']:
    # print(key)
    if key['visitorId'] != new_dict:
        new_dict['sessionByUser'] = [key['visitorId']]
        for x in new_dict['sessionByUser']:
            new_dict[x] = [key['url']]
    else:
        new_dict['sessionByUser'] = [key['visitorId']]

print(new_dict)