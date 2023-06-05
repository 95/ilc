from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, color, vin):
        self.color = color
        self.vin = vin

    @abstractmethod
    def start_engine(self):
        pass

    def honk(self):
        print("Honk!")

class Car(Vehicle):
    def __init__(self, color, model, vin):
        super().__init__(color, vin)
        self.model = model

    def start_engine(self):
        print(f"The {self.model}'s engine starts.")

    def drive(self):
        print(f"The {self.model} is driving.")

class Tesla(Car):
    def __init__(self, color, model, vin, autopilot):
        super().__init__(color, model, vin)
        self.autopilot = autopilot

    def start_engine(self):
        print(f"The electric engine of {self.model} starts silently.")

    def activate_autopilot(self):
        if self.autopilot:
            print(f"{self.model} is on autopilot mode.")
        else:
            print(f"This {self.model} does not have an autopilot feature.")

class Fleet:
    def __init__(self):
        self.fleet = []

    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)

    def list_fleet(self):
        for vehicle in self.fleet:
            print(f"Model: {vehicle.model}, Color: {vehicle.color}, VIN: {vehicle.vin}")

    def find_vehicle_by_vin(self, vin):
        for vehicle in self.fleet:
            if vehicle.vin == vin:
                return vehicle
        return None


my_fleet = Fleet()

my_fleet.add_vehicle(Tesla("red", "Model 3", "EXAMPLEVIN", True))
my_fleet.add_vehicle(Tesla("blue", "Model S", "EXAMPLEVIN", False))
my_fleet.add_vehicle(Car("green", "Toyota Corolla", "EXAMPLEVIN"))

my_fleet.list_fleet()

car = my_fleet.find_vehicle_by_vin("EXAMPLEVIN")
if car:
    car.start_engine()  
