#recursion function apny aap ko hi call krta hai
#program of factorial
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1) #yaha ppar function khud ko call krega jo ki recursion kahlata hai
n=int(input("ENTER A NUMBER: "))
print(f"the factorial of the given number is :  {factorial(n)}")