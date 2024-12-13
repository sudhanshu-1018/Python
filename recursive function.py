#Factorial
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
a=int(input("enter the number that you want factorial of:"))
print(factorial(a))
    

#Fibonacci sequence
def F(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return F(n-1)+F(n-2)
    
b=int(input("Enter the number that you want Fibonacci sequence of:"))
print(F(b))
    
