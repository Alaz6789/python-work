class Vehicle:
    def __init__(self):
        print("This is the parent class")
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("This is the child class")
    def honk(self):
        print("The car goes honk!")

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        print("This is the child class")
    def kick_start(self):
        print("The bike has kick started!")

Alphad = Car()
Carrera = Bike()

Alphad.move()
Carrera.move()
Alphad.honk()
Carrera.kick_start()