from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self._name = name  
   
    @abstractmethod
    def make_sound(self):  
        pass

    @property
    def name(self):  
        return self._name

    @name.setter
    def name(self, name):  
        self._name = name


class Dog(Animal):
    def make_sound(self): 
        return 'woof!'


class Cat(Animal):
    def make_sound(self):  
        return 'meow'


dog = Dog("pixie")
cat = Cat("whiskerton")

animals = [dog, cat]
for animal in animals:
    print(f'{animal.name} says {animal.make_sound()}')

dog.name = "pickles"
print(f'{dog.name} says {dog.make_sound()}')
