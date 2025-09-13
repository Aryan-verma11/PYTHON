s={1,4,5}   #sets are also use {} s={}then it wil be a empety dict


e=set() #this is empty set you have to write that it is empty set
#no any element is repeates in set 

a={2,2,2,2,4,4,4,4,5,5,5}
print(a) 
#set methods

b={1,2,3,4,5,"aryan"}
print(b)
b.add(6)
print(b,type(b))

#sets are unordered , no way to change existing daata , no duplicate value, 
b.remove(1)
print(b)
b.pop()
print(b)
 
 #union and intersection 
s1={1,45,6,78}
s2={7,8,1,78}
print(s1.union(s2))
print(s1.intersection(s2)) #overlapping values ho 
