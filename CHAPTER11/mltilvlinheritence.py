class employee:
    a=1

class programmer(employee):
    b=2

class manager(programmer):
    c=3


o=employee()
print(o.a)
#we cannt print b or c in the employee class

o=programmer() 
print(o.a,o.b)


o=manager()
print(o.a,o.b,o.c)