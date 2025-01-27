class Car:
    def __init__(self, brand: str, model: str, year: int, price: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - ${self.price}"


class CarShowroom:
    def __init__(self, name: str):
        self.name = name
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def sell_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Автомобіль {car} продано!")
        else:
            print(f"Автомобіль {car} відсутній у салоні.")

    def __str__(self):
        cars_info = "\n".join(str(car) for car in self.cars)
        return f"Car Showroom {self.name}:\n{cars_info if self.cars else 'No cars available.'}"


# Приклад використання
car1 = Car("Toyota", "Camry", 2020, 25000)
car2 = Car("BMW", "X5", 2021, 60000)
car3 = Car("Tesla", "Model 3", 2022, 45000)

showroom = CarShowroom("Dream Cars")
showroom.add_car(car1)
showroom.add_car(car2)
showroom.add_car(car3)
print(showroom)

showroom.sell_car(car2)
print(showroom)
