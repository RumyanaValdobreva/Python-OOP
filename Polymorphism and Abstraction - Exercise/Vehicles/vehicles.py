from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        if self.fuel_quantity / (self.fuel_consumption + 0.9) >= distance:
            self.fuel_quantity -= distance * (self.fuel_consumption + 0.9)

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        if self.fuel_quantity / (self.fuel_consumption + 1.6) >= distance:
            self.fuel_quantity -= distance * (self.fuel_consumption + 1.6)

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * 0.95