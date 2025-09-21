a=89    #here it is a global variable which you can use inside aur outside the function
def fun():
    a=3
    print(a)

fun()
print(a)