class Employee:
    language ="py"  
    salary = 120000

    def __init__(self ,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language           
        print("i am creating an object")
# __ sy start hony waly methods ko DUNDUR method kahty hai aur ye automatically call ho jaty hai 
#jab bhi aap ek new object bnaogy tab ye dundur method automatically call ho jayega 


    def getinfo(self):
        print(f"the language is {self.language}, the salry is {self.salary}")


    @staticmethod   
    def greet(self):
        print("good morning")


aryan = Employee("aryan",130000,"js")
# aryan.name="aryan"
print(aryan.name,aryan.salary,aryan.language)

kammo = Employee("kammo",100000,"cpp")

print(kammo.name,kammo.salary,kammo.language)
