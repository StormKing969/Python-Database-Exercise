import requests
import json

data = requests.get("https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=09fc3b3c9df37bf824f90d470a4f")
print(data)