class Human:
    #1 constructor
    def __init__(self, nameValue, ageValue):
        #2 property
        self.name = nameValue
        self.age = ageValue
        print("Constructor is called")
    
    #3 behaviour
    def sleep(self):
        print("Human is sleeping")

    def eat(self):
        print(self.name, "is eating")

# object
alif = Human("Alif Azhar", 14)
akash = Human("Akash Kumar Roy", 48)
print(alif.name)

akash.eat()
alif.eat()