l=[1,2,3,4,5,6,7,8]
print(type(l))
print(l)

l.append(9)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

l.insert(2,18)
print(l)

m=[19,20,21]
l.extend(m)
print(l)

k=m+l
print(k)

l.pop(4)
print(l)

print(l.index(5))

print(l.count(6))

m=l
m[0]=0
print(l)

m=l
m[0]=0
print(m)

m=l.copy()
m[0]=1
print(m)

text=["sudhanshu","raushan","suman","santu","harsh","vishal","hrishikesh"]
text=[x+" shoutout" for x in text]
# new_list = []
# for x in text:
#   new_list.append(x+' word')
# my_list = new_list[:]