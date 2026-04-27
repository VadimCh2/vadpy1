import requests

url = 'https://script.google.com/macros/s/AKfycbygyFTYWMm5eRoLmvyI8S5pjWLPj-H3LOFDocJPorQsbV-OGaRRJ7DhsR8faoutWTf9/exec'

response = requests.get(url=url, params={})
response_json = response.json()
venomous_care_cost = 0
animals = response_json['animals']
african_animals = 0

for row in animals:
    if row['is_venomous'] == 'yes':
        venomous_care_cost += row['care_cost'] * row['count']
    if row['continent'] == 'africa':
        african_animals += row['count']

print(f'{african_animals}')
print(f'{venomous_care_cost}')
