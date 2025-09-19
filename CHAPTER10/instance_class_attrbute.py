class Employee:
    languauge ="py" #this is class attribuite 
    salary = 120000
aryan = Employee()
aryan.name ="aryan"#this is instance attribute bcz it is applied in the class after making the object 
print(aryan.name,aryan.languauge,aryan.salary)

tanu=Employee()
tanu.name="kammo madam ji"
print(tanu.name, tanu.salary, tanu.languauge)

#instance have more priority than class attribute there in below code the language is changed to java in instance attribute


kammo=Employee()
kammo.languauge="javascript"
print( kammo.salary, kammo.languauge)
