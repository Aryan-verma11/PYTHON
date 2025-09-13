marks = {
    "aryan":98,
    "ajay":78,
    "aman":87,
    "rohan":56,
    0:"ritik"

}
print(marks.items()) #it prints all key value pairs
print(marks.keys()) #it prints all key  pairs
print(marks.values()) #it prints all value  pairs
marks.update({"aryan":99,"tanu":67})
print(marks) #this proves that dict are mutable and you can add or update the dict
print(marks.get("aryan")) ##if the given name doesnt exist than it will give you none
print(marks["aryan"]) #if the given name doesnt exist than it will give you error