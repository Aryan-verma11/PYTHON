a=int(input("enter a number: "))
b=int(input("enter a number: "))

if b==0:
    raise ZeroDivisionError("This is not your fathers property so please enter non zero number")
else:
    print(f"the dividion a/b is {a/b}")