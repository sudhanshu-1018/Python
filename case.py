x=int(input("enter the number x:"))
# x is the variable to match
match x:
    #if x is o
    case 0:
        print("case is 0")
    case 4:
        print("case is 4")
    case _ if x==5:
        print("case is 5")
    case _ if x>5 and x<=10:
        print("case is between 6 to 10")
    case _ if x!=11:
        print(x,"is not 11")
    case _:
        print(x)

    