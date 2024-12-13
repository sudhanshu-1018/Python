dic={"name":"sudhanshu kumar singh","age":18,"eligibility":True}
print(dic)
print(dic["name"])
# print(dic["sudhanshu kumar singh"])   # (wrong)
print(dic.get("name2"))
print(dic.values())
print(dic.keys())

for key in dic.keys():
    print(dic[key]) #FOr Value
    print(key) #for key
    
for value in dic.values():
#     # print(dic[value])   # (wrong)
    print(value)

print(f"The value correspondence to {key} is {dic[key]}")
print(f"The value correspondence to {key} is {value}")        #(For this [for value in dic.values()])

print(dic.items())
for key,value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")




ep1={233:98,394:56,495:87}
ep2={434:30,394:55}

ep1.update(ep2)
print(ep1)

# ep1.clear()
# print(ep1)

ep1.pop(233)
print(ep1)

ep1.popitem()
print(ep1)

del ep1[394]
print(ep1)

# del ep1
# print(ep1)