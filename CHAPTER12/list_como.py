#list comprehnsion

mylist=[1,2,3,4,5,6,7]
# squaredlist=[]
# for item in mylist:
#     squaredlist.append(item*item)



#this work can be done in one line by list comprehnsion

squaredlist=[i*i for i in mylist]
print(squaredlist)