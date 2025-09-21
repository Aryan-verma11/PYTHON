def main():
    try:
        a=int(input("enter a number: "))
        print(a)
        return

    except Exception as e:
      print (e)
      return

    finally:
      print("i am inside finally")

main()


# print("i am inside finally")



#finally ka use aata hai function me sare niyam tod ke chalega hi chalega 