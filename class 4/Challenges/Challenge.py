class Student:
    def __init__(self, nameValue, gradeValue, subjectValue):
        self.name = nameValue
        print("This students name is", self.name)
        self.grade = gradeValue
        print(self.name, "got", self.grade)
        self.subject = subjectValue
        print(self.name, "takes", self.subject)

    def study(self):
        print(self.name, "is studying", self.subject)

    def introduce(self):
        print("This students name is", self.name, ", he takes", self.subject, "and got", self.grade)

Alif = Student("Alif Azhar", "97%", "Maths")
Akash = Student("Akash Kumar Roy", "100%", "Computer Science")
John = Student("John Dalton", "93%", "Physics")

Alif.study()
Akash.introduce()