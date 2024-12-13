def func1():
    try:
        l=[1,5,6,7]
        i=int(input("Enter the index"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    # print("I am not always executed")
    finally:
      print("I am always executed")

# print(func1())
x=func1()
print(x)

#project
a=input("Enter quit to exit:")
try:
    for i in a:
     if a=="quit":
        print("you are now exit")
     break
except:
   print("invalid input")

finally:
   print("see you next time")
