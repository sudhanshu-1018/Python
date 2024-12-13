import os
files=os.listdir("data/Day1")
i=1
for file in files:
    if file.endswith(".jpeg"):
     print(file)
     os.rename(f"data\Day1/{file}",f"D:data\Day1/{i}.jpeg")
     i=i+1