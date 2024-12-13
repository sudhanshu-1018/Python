# import os
# # os.mkdir("data")
# if (not os.path.exists("data")):
#     os.mkdir("data")             #create file
# for i in range(0,10):
#     os.mkdir(f"data/Day{i+1}")
#     # os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}")


import os
folders=os.listdir("data")
print(folders)

for folder in folders:
    print(folder)
    
    # print(os.listdir(f"data/{folder}"))