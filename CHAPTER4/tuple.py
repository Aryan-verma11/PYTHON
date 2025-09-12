# tuples are immutable made by using ()
b=()
print(type(b))
# tuple with a single element 
c=(9,)
print(type(c))

a=(1,23,45,76,24,85,3,5,"rohan",6.6,False,"shivam")
print(type(a))
# a[0]=2 this will not work bczz because tuples are immutable we cant change even string
print(a)
p=a.count(45)
print(p)
print(1 in a)
print(len(a))
a1,b1,c1=(1,2,3)
print(a1)