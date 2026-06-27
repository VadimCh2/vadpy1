class Car:
    def __init__(self, model: str, age: int, owner: str = "", fuel: int = 0):
        self.model = model.strip().title()
        self.age = age
        self.owner = owner
        self.fuel = fuel
        self.car_id = id(self)

    def __str__(self) -> str:
        return f"<{self.model}: {self.car_id}. Fuel: {self.fuel}L>"

    def add_fuel(self, amount: int):
        self.fuel += amount

    @property
    def car_state(self) -> str:
        if self.age <= 3:
            return "Нове авто"
        elif self.age <= 10:
            return "Середній стан"
        else:
            return "Старе авто"

    @property
    def fuel_status(self) -> str:
        if self.fuel < 15:
            return "Потрібно заправитись"
        elif self.fuel < 40:
            return "Достатньо бензину"
        else:
            return "Можна їхати далеко"


car_1 = Car(model="bmw", age=2, owner="Alex")
car_2 = Car(model="audi", age=12, owner="Ivan", fuel=30)

print(id(car_1))
print(id(car_2))

print(car_1.__dict__)
print(car_2.__dict__)

print(car_1)
print(car_2)

car_1.fuel += 10
print(car_1)

car_1.add_fuel(20)
print(car_1)

print(car_1.car_state)
print(car_2.car_state)

print(car_1.fuel_status)
print(car_2.fuel_status)

if car_1.fuel > car_2.fuel:
    print(f"{car_1.model} має більше бензину.")
elif car_1.fuel < car_2.fuel:
    print(f"{car_2.model} має більше бензину.")
else:
    print("В обох авто однакова кількість бензину.")