class Employee:
    name="default name"
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class coder:
    lang="python"
    def printlanguages(self):
        print(f"out of all language here is your language: {self.lang}")


class programmer(Employee,coder):
    company="ITC Infotech"
    def showlang(self):
        print(f"The company name is {self.company} and the company is {self.lang} and he is good with")


a=Employee()
b=programmer()


b.show()
b.printlanguages()
b.showlang()
