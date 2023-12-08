class Animal:
    @staticmethod
    def tell():
        print("Animal sound")


class Dog(Animal):
    @staticmethod
    def tell():
        print("Woof")


class Cat(Animal):
    @staticmethod
    def tell():
        print("Meow")


def speak(obj: Animal):
    obj.tell()
