marks=[12,34,45,98,34,55,87]
index=0
for mark in marks:
    print(mark)
    if index==3:
        print("sudhanshu awesome!")
    index+=1


for index,mark in enumerate(marks):
    print(mark)
    # print(index,mark)
    if index==3:
        print("sudhanshu is awesome!")



for index,mark in enumerate(marks,start=1):
    # print(mark)
    print(index,"-",mark)
    if index==3:
        print("sudhanshu is awesome!")
