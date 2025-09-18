'''
a="a very long string with emails
emails=[]
 3 seconds liye program ko chalny me 
 program chala emails read hue aur program khatm kahi bhi data save nhi hota hai 
 but a pyrhon program in python can save it aur we can read and write with the help of fiel
'''

f=open("file.txt")
data=f.read()
print(data)
f.close()




#pyhton me do tarah ki files hoti hai
# pahla text files 
#dusra binary files
#ismy bhot sare built in function hoty hai 
#1.open 
#ye do parameters leta haio ek file ka naam aur ek mode by default function read hota hai

f=open("file.txt","r")
data=f.read()
print(data)
f.close()