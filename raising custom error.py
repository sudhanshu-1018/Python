a=int(input("enter any value between 5 and 9"))
if a<5 or a>9:
    raise ValueError("value should be between 5 and 9")


#Defining custom exception (creating a new class for making own custom error)
class customError():
    #code
    pass

try:
    #code
except customError():
    #code

