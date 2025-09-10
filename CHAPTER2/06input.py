a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))

print("Number a is: ",a)
print("Number b is: ",b)
print("sum of number is: ",a+b)

# here the output is joined together bcz input is taken as string and the + operator concatinate the both a and b
# therefor we get a b instead of a+b for getting the sum of both a and b we have to tell the input that take it as 
# integer not as a string
a=input("Enter 1st name: ")
b=input("Enter 2nd name: ")
print("name is: ",a+b)