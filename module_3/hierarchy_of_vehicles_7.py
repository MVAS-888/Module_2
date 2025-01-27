class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors


class Bike(Vehicle):
    def __init__(self, brand, model, year, type_of_bike):
        super().__init__(brand, model, year)
        self.type_of_bike = type_of_bike
