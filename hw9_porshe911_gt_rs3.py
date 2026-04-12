# 1.
porshe_911_gt_rs3 = {
    "model": "Porshe 911 GT3 RS",
    "price": 14030000,
    "displacement": "3 996 cm³",
    "weight": "1 450 kg",
    "max_speed": "296 km/h",
    "fuel_consumption": 13.2,
    "interior_features": [
        "Шкіряні спортивні сидіння",
        "Мультимедійна система",
        "Підігрів сидінь"
    ],
    "trunk": {
        "volume": "125l",
        "folded_seats_volume": "250 л"
    }
}
# 2. Немає причепа
car_model = porshe_911_gt_rs3.get("model")
print(car_model)
car_price = porshe_911_gt_rs3.get("price")
print(car_price)
first_feature = porshe_911_gt_rs3.get("interior_features")[0]
print(first_feature)
folded_trunk = porshe_911_gt_rs3.get("trunk").get("folded_seats_volume")
print(folded_trunk)

insurance = porshe_911_gt_rs3["price"] * 0.005
porshe_911_gt_rs3["insurance_payment"] = insurance
print(insurance)

trip_cost = 2 * porshe_911_gt_rs3["fuel_consumption"] * 93
print("Вартість подорожі на 200 км:", trip_cost, "грн")
