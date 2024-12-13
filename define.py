#Basic of define
def hello():
   print("hello everyone")

hello()


def ssd(fx):
    return fx*4

print(ssd(5))


cube=lambda x:x*x*x
print(cube(5))
def appl(fx,value):
   return fx(value)# return cube(5)
print(appl(cube,5))


#The function greet takes another function as its argument, fx, and defines a nested function, mfx, inside it.
#The nested function mfx prints “good morning”, then calls the original function fx, and then prints “thanks for using this function”.
#The function greet returns the nested function mfx as its output.
def greet(fx):
   def mfx():
      print("good moring")
      fx()
      print("thanks for using this function")
   return mfx
@greet
def hello():
   print("hello")
hello()

# *tuple
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
     sum=sum+i
    print(sum/len(numbers))

average(2,5)


# **dictionary
def name(**name):
   print(type(name))
   print("Hello,",name["fname"],name["mname"],name["lname"])

name(fname="sudhanshu",lname="singh",mname="kumar")


marks=[3,5,6,8,9,4,0,"hello",True]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[-5])
if 7 in marks:
   print("Yes")
else:
   print("No")
print(marks[1:8])
#jump index
print(marks[1:8:3])


lst=[i for i in range(4)]
print(lst)

lst2=[i*i for i in range(10)if i%2==0]
print(lst2)
