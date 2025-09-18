f=open("file.txt","r")
# # lines=f.readlines()
# line1=f.readline()
# print(line1,type(line1))
# line2=f.readline()
# print(line2,type(line2))
# line3=f.readline()
# print(line3,type(line3))
# line4=f.readline()
# print(line4,type(line4))
# line5=f.readline()
# print(line5,type(line5))
# f.close()

# doing all these stuff in while loop


line=f.readline()
while(line !=""):
    print(line)
    line = f.readline()
f.close()

#  r **Read-only mode** (default). File must exist.   


# w  **Write-only mode**. Creates a new file or truncates if it exists.  

                
# x **Exclusive creation**. Fails if the file already exists.



# a  **Append mode**. Creates the file if it doesn't exist, otherwise writes at the end.
