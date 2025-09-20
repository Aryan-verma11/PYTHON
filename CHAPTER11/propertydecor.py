
class number:
    a=2
    @classmethod
    def show(cls):
         print(f" now, this is an class attribute {cls.a}")
    @property
    def name(self):
         return self.name1
    @name.setter
    def name(self,value):
         self.name1=value.split(" ")[0]
         self.name2=value.split(" ")[1]


o=number()
o.a=23

name1="aryan verma"
print(name1)

o.show()