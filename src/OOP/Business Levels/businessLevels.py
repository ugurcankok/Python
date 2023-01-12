class Worker:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showInformation(self):
        print("Showing the Information.....")
        print("Name: ", self.name, " Salart: ", self.salary, " Department: ", self.department)

    def raiseAmount(self, raise_amount):
        print("Your salary is raising...")
        self.salary += raise_amount

    def changeDepartment(self, new_department):
        print("Changing the your department....")
        self.department = new_department


class Executive(Worker):
    def __init__(self, name, salary, department, numberOfPeople):
        # overriding
        super().__init__(name, salary, department)
        self.numberOfPeople = numberOfPeople  # add another property

    def showInformation(self):
        # overriding
        print("Showing the Informations For Execute Level...")
        print("Name: ", self.name, " Salary: ", self.salary, " Department: ", self.department, " Number of People: ",
              self.numberOfPeople)


executive = Executive("ugur", 5000, "Computer", 20)
executive.showInformation()
