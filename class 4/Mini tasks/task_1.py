class Car:
    def __init__(self, brandValue, modelValue, yearValue):
        self.brand = brandValue
        print("The brand is ", self.brand)
        self.model = modelValue
        print("The model is ", self.model)
        self.year = yearValue
        print("It was made in the year", self.year)

    def drive(self):
        print(self.brand, self.model, " is driving")

    def brake(self):
        print(self.brand, self.model," has braked")

Car1 = Car("BMW", "Model 2", "2024")
Car2 = Car("Mercedes", "Model S", "2022")

Car1.drive()
Car2.brake()