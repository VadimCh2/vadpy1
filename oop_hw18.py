from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self,model: str, fuel: int,condition: int ):
        self.model = model
        self.fuel = fuel
        self.condition = condition

    @property
    def is_working(self) -> bool:
       return self.condition >= 10
    @property
    def is_enough_fuel(self) -> bool:
        return self.fuel > 0

    @abstractmethod
    def __str__(self) -> str:
        return ''

    def move(self, distance: int):
        if not self.is_working:
            print("Not working")
            return

        if self.fuel < distance:
            print("Not enough fuel")
            return

        self.fuel -= distance
        self.condition -= distance * 0.5

        print(f"Moved {distance} km")
class Car(Transport):
    def __init__(self, model: str, fuel: int = 50, condition: int = 100):
        super().__init__(model, fuel, condition)
        self.model = model

    def __str__(self):
        return f"Car: {self.model}, fuel: {self.fuel}, condition: {self.condition}"

class Truck(Transport):
    def __init__(self, name: str, fuel: int = 120, condition: int = 100):
        super().__init__(name, fuel, condition)
        self.name = name

    def __str__(self):
        return f"Truck: {self.name}, fuel: {self.fuel}, condition: {self.condition}"

class Motocycle(Transport):
    def __init__(self, brand: str, fuel: int = 20, condition: int = 100):
        super().__init__(brand, fuel, condition)
        self.brand = brand

    def __str__(self):
        return f"Motocycle: {self.brand}, fuel: {self.fuel}, condition: {self.condition}"

class ServiceStation():
    def repair(self,transport_unit: Transport):
        transport_unit.condition += 20



car = Car('X')
truck = Truck('bro')
motorcycle = Motocycle('Kawasaki')
station = ServiceStation()
print(car.is_working)
print(truck.__dict__)
car = Car('X',fuel = 0)
print(car)
car.move(20)
truck = Truck('bro',condition=9)
truck.move(20)
station.repair(car)
print(car)
station.repair(motorcycle)
print(motorcycle)
station.repair(truck)
station.repair(truck)
station.repair(truck)
print(truck)