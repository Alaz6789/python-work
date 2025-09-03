class Animal:
    def __init__(self, nameValue, soundValue):
        self.name = nameValue
        print("The name of the animal is ", self.name)
        self.sound = soundValue
        print("The sound the ", self.name, " makes is a ", self.sound)

    def make_sound(self):
        print("The", self.name, "makes a ", self.sound, "sound")

Dog = Animal("Dog", "Woof")
Cat = Animal("Cat", "Meow")

Dog.make_sound()
Cat.make_sound()