porshe_911_gt_rs3 = {
    "model": "Porshe 911 GT3 RS",
    "price": 14030000,

    "displacement": 3996,
    "weight": 1450,
    "max_speed": 296,

    "fuel_consumption": 13.2,

    "interior_features": [
        "Шкіряні спортивні сидіння",
        "Мультимедійна система",
        "Підігрів сидінь"
    ],
    "trunk": {
        "volume": 125,
        "folded_seats_volume": 250
    }
}

# 2. Немає причепа
car_model = porshe_911_gt_rs3.get("model")
print(car_model)

car_price = porshe_911_gt_rs3.get("price")
print(car_price,"грн")

first_feature = porshe_911_gt_rs3.get("interior_features")[0]
print(first_feature)

folded_trunk = porshe_911_gt_rs3.get("trunk").get("folded_seats_volume")
print(folded_trunk,"л")

insurance = porshe_911_gt_rs3["price"] * 0.005
porshe_911_gt_rs3["insurance_payment"] = insurance
print(insurance,"грн")

trip_cost = 2 * porshe_911_gt_rs3["fuel_consumption"] * 93
print("Вартість подорожі на 200 км:", trip_cost, "грн")