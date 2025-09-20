# class method ek tarika hai jis sy ek method ke andar class ko directly access kr skta hoon
# jaisa ki hum janty hai ki class me class attribute sy jyda instance attribute ko prference mil jati hai lkin agar hmey class attribute ko preference deni hoto hum @classmethod ka use krengy aur self ki jagah (cls) ka use karengy



# class number:
#     a=2
#     def show(self):
#         print(f"this is an instance attribute {self.a}")

# o=number()
# o.a=23

# o.show()




class number:
    a=2
    @classmethod
    def show(cls):
         print(f" now, this is an class attribute {cls.a}")

o=number()
o.a=23

o.show()