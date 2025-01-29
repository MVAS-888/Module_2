# Завдання 1: Клас "Автомобіль" з інкапсуляцією атрибутів і методів доступу
class Car:
    def __init__(self, make, model, year, color):
        self.__make = make 
        self.__model = model  
        self.__year = year  
        self.__color = color  

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_color(self, color):
        self.__color = color

# Завдання 2: Класи для мов та метод greeting
class English:
    def greeting(self):
        return "Hello, friend!"

class Spanish:
    def greeting(self):
        return "¡Hola, amigo!"

def hello_friend():
    english = English()
    spanish = Spanish()
    print(english.greeting())
    print(spanish.greeting())

car = Car("Toyota", "Corolla", 2021, "blue")
print(car.get_make())
car.set_color("red")
print(car.get_color())

hello_friend()        