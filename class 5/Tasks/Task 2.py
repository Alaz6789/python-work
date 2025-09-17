class Animal:
    def __init__(self):
        print("Parent")
    def eat(self):
        print("Animal is eating!")
    
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Child")
    def bark(self):
        print("Dog is Barking!")

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Child")
    def meow(self):
        print("Cat is meowing!")

Doug = Dog()
Elsa = Cat()

Doug.eat()
Elsa.eat()

Doug.bark()
Elsa.meow()