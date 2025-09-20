class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


#nichy diye gaye syntax me class programmer(Employee):  likhny sy employee class ki sari properties inherit kar jayengi programmer class me sare methoda aur attribute bhi


class programmer(Employee):
    company="ITC Infotech"
    def showlang(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


a=Employee()
b=programmer()
print(a.company,b.company)