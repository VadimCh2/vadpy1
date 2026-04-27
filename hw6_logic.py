import math
from hw6_config import *

def calculate_trip(students, teachers, transport, days):
    if students == 0:
        return {"error": "Кількість учнів не може бути 0"}

    total_people = students + teachers

    buses = 0
    transport_cost = 0

    if transport == "Автобус 🚌":
        buses = math.ceil(total_people / BUS_CAPACITY)
        transport_cost = buses * BUS_PRICE
    else:
        transport_cost = total_people * TRAIN_PRICE_PER_PERSON

    if days == 0:
        living_cost = 0
    else:
        living_cost = total_people * HOTEL_PRICE_PER_NIGHT * days

    total_cost = transport_cost + living_cost

    discount = 0
    if total_people > 30:
        discount = total_cost * 0.1
        total_cost *= 0.9

    return {
        "total_people": total_people,
        "buses": buses,
        "transport_cost": transport_cost,
        "living_cost": living_cost,
        "discount": int(discount),
        "total_cost": int(total_cost),
        "transport": transport
    }