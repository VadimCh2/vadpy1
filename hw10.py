import requests
from pprint import pprint

url = 'https://dummyjson.com/recipes'

response = requests.get(url=url)
response_json = response.json()
cuisine = response_json['cuisine']

count = 0

for all_cuisines in cuisine:
    if all_cuisines['cuisine'] == count:
        count += 1