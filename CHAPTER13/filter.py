l=[1,2,3,4,5,6]
def even(n):
    if (n%2==0):
        return True
    return False
onlyeven=filter(even,l)
print(list(onlyeven))
