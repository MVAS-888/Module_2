# Завдання 3: Клас, що описує температуру з властивостями для шкал Цельсія та Фаренгейта
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Завдання 4: Класи Base і Child з використанням classmethod декоратора
class Base:
    @classmethod
    def method(cls):
        print("Hello from Base")

class Child(Base):
    @classmethod
    def method(cls):
        print("Hello from Child")

temp = Temperature(25)
print(f"Цельсій: {temp.celsius}, Фаренгейт: {temp.fahrenheit}")

temp.fahrenheit = 100 
print(f"Цельсій: {temp.celsius}, Фаренгейт: {temp.fahrenheit}")

Base.method()
Child.method()
