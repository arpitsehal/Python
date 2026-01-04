#function overriding example
# class Animal:
#     def make_sound(self):
#         print("Some generic animal sound")

# class Dog(Animal):
#     def make_sound(self):  #overriding the method
#         print("Bark")
# class Cat(Animal):
#     def make_sound(self):  #overriding the method
#         print("Meow")
# animal = Animal()
# animal.make_sound()
# dog = Dog()
# dog.make_sound()
# cat = Cat()
# cat.make_sound()

#ducking typing example
class Bird:
    def fly(self):
        print("Bird is flying")
class Airplane:
    def fly(self):
        print("Airplane is flying")
def let_it_fly(flying_object):
    flying_object.fly()
bird = Bird()
airplane = Airplane()
let_it_fly(bird)
let_it_fly(airplane)


