class employee:
    def __init__(self):
        print("The constructor of Employee")
    a=1

class programmer(employee):
     def __init__(self):
        print("The constructor of Programmer")
     b=2

class manager(programmer):
     def __init__(self):
        super().__init__()
        print("The constructor of Manager")
     c=3


# o=employee()
# print(o.a)
# #we cannt print b or c in the employee class

# o=programmer() 
# print(o.a,o.b)


o=manager()
print(o.a,o.b,o.c)


#agar hmmey sirf super class run krni ho mtlb sirf ek step oopr ki class run krni ho tb hum super().__init__() ka use karty hai