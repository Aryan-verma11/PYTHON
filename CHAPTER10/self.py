class Employee:
    language ="py"  
    salary = 120000

    def getinfo(self):
        print(f"the language is {self.language}, the salry is {self.salary}")


    @staticmethod   #jab kisi function ko object ki jaroorat na padey aur ye method ak decorator hota hai
    def greet(self):
        print("good morning")


aryan = Employee()
#yeh nichy diya hua syntaxc employee.getinfo(aryan) me convert ho jata hai yaha humny ek arguemeny diya hai jo ki accept nhi hua hai accept krany ke liye hmmey self ka use krna hoga function me
aryan.greet()
aryan.getinfo()

# Employee.getinfo(aryan)

