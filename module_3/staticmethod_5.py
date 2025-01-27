class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult_ukraine(age):
        return age >= 18

    @staticmethod
    def is_adult_usa(age):
        return age >= 21
