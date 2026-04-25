import requests

url = 'https://dummyjson.com/recipes'

response = requests.get(url=url)
response_json = response.json()

pizza_count = 0
cuisine_count = 0
cooking_190 = []
total_reviews = 0


most_caloric = response_json["recipes"][0]

for recipe in response_json["recipes"]:

    if "pizza" in recipe["name"].lower():
        pizza_count += 1

    if recipe["cuisine"].lower() == "italian":
        cuisine_count += 1

    if recipe["caloriesPerServing"] > most_caloric["caloriesPerServing"]:
        most_caloric = recipe

    if "190" in recipe["instructions"][0]:
        cooking_190.append(recipe["name"])
    total_reviews += recipe["reviewCount"]

print("Кількість піц:", pizza_count)
print("Італійських страв:", cuisine_count)
print("Найкалорійніша страва:", most_caloric["name"])
print("Калорії:", most_caloric["caloriesPerServing"])
print("Всього переглядів:", total_reviews)
print("Страви при 190°C:")
for recipe2 in cooking_190:
    print(recipe2)