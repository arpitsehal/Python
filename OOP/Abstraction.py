#hiding internal details and showing only functionality to the user
#abstract classes can be created using abc module
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Lion(Animal):
    def make_sound(self):
        print("Roar")
class Dog(Animal):
    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def make_sound(self):
        print("Meow")

lion = Lion()
lion.make_sound()

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()
