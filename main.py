from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print("This car goes.")


class Motorcycle(Vehicle):
    def go(self):
        print("This motorcycle goes.")


car = Car()
car.go()

motorcycle = Motorcycle()
motorcycle.go()
