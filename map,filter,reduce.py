def cube(a):
    return a*a*a

print(cube(2))

l=[1,2,3,4,5,6,7,8]
newl=[]

# loop + append
for item in l:
    newl.append(cube(item))
print(newl)

# map
newl=list(map(cube,l))
print(newl)

# map + lambda
newl=list(map(lambda x:x*x*x,l))
print(newl)

# filter
def filter_function(b):
    return b>4

print(filter_function(4))
f=[1,2,3,4,5,6,7,8]
value=list(filter(filter_function,f))
print(value)

# filter + lambda
value=list(filter(lambda x:x>4,f))
print(value)

# reduce

from functools import reduce
def mysum(x,y):
    return x+y
numbers=[1,2,3,4,5,6,7,8]
sum=reduce(mysum,numbers)
print(sum)

sum=reduce(lambda x,y:x+y,numbers)
print(sum)
