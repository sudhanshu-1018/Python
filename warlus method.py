a=True
print(a==False)
print(a:=False)
print(a==True)     #return false here(opposite)
print(a:=True)

# print(c=True)   # not printable
# print(c==True)  # not printable

print(d:=True)  # printable



numbers=[1,2,3,4,5]
while(len(numbers))>0:
    print(numbers.pop())


numbers=[1,2,3,4,5]
while(n:=len(numbers))>0:
    print(numbers.pop())


# numbers=[1,2,3,4,5]
# while(n==len(numbers))>0:     # not printable (n is not defined)
#     print(numbers.pop())


# foods=list()
# while True:
#     food=input("what food do you like?")
#     if food=="quit":
#         break
#     foods.append(food)
        
foods=list()
while(food:=input("what food do you like?:"))!="quit":       #short way of writing above foods=list()
    foods.append(food)
