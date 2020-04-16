
class Calısan():
    def __int__(self,name,lastname,salary,experience,department):
        self.name=name
        self.lastname=lastname
        self.salary=salary
        self.experience=experience
        self.department=department

    def increaseSalary(self,raise_ratio):
        self.salary+=raise_ratio

    def change_department(self,new_department):
        self.department=new_department

    def showPerson(self):
        print("Name:",self.name,"Lastname:",self.lastname,"Salary:",self.salary,"Experince:",self.experience,
              "Department:",self.department)



class Manager(Calısan):
    def __init__(self,name,lastname,salary,experience,department,person_number):

        super().__int__(name,lastname,salary,experience,department)

        self.person_number=person_number

    def showPerson(self):
        return  super().showPerson(),
        print("Person Number:",self.person_number)



manager=Manager("ugurcan","kök",10000,10,"computer engineer",10)
manager.showPerson()
manager.increaseSalary(1000)
manager.showPerson()
