with open("file.txt","r") as f:
    f.seek(10)
    print(f.tell())
    data=f.read(5)
    print(data)

# truncate function
with open('file.txt','w') as d:
    d.write("how are you")
    d.truncate(5)