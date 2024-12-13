# Notice that the code inside the if __name__ == "__main__" block in hello.
# py is only executed when the file is run as a script. If you try to import it from another file, such as main.py, nothing will happen.

# The reason for this is that when you import a module, Python sets the special variable __name__ to the name of the module. For example,
# if you import hello.py, then __name__ will be "hello".
# However, when you run a script directly with Python or Python3, then __name__ will be set to "__main__".
#  This way, you can check whether your file is being run as a script or imported as a module by using an if statement like this:



# check if __name__ is "__main__":
if __name__ == "__main__":
    # do something only when running as a script
    print("This code runs only when running as a script.")
else:
    # do something else when imported as a module
    print("This code runs only when imported as a module.")

print(type(__name__=="__main__"))                                        #type is boolen (True or false)