# polymorphism
# Employeee Managemet
#  Employee 
# polymorphism: poly --> many , morph---> form: overridng
class Employee:
    def __init__(self,nameV,idV):
        self.name = nameV
        self.id = idV
        print("Emp constructor")
    def displayInfo(self):
        print(f"empl name is :{self.name}\nid: {self.id}\n---")

# child --->
class Manager(Employee):
    def __init__(self,nm,id,dprt):
        super().__init__(nm,id)
        self.department = dprt
        print("manager class constructor is called")
    def displayInfo(self):
         super().displayInfo()
         print(f"department is {self.department}")

class AndroidDeveloper(Employee):
    def __init__(self,nm,id,tcst):
        super().__init__(nm,id)
        self.techstat = tcst
        print("Android developer")
    def displayInfo(self):
        super().displayInfo()
        print(f"Techstat is {self.techstat}")
    
     
alif = Manager("Alif Azher","Emp0011","Android")
alif.displayInfo()

ammar = AndroidDeveloper("Ammar Azhar", "Emp0012", "KMM")
ammar.displayInfo()