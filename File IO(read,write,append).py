f=open("myfiles.txt","r")
text=f.read()
print(text)
f.close()

#open new txt file
f=open("file.txt","w")
f.write("hello,world!")
f.close()

#'with' statement
# NO need to close()
with open ("myfiles.txt","a") as f:
    f.write("\nhey I am inside with")


