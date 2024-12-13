
# The output shows that the str() function calls __str__() and returns a human-friendly string, while the repr() function calls __repr__()
# and returns a more information-rich string that can be used to recreate the object.
# In fact, you can use the repr() function with the eval() function to create a new object from the string:

import datetime

mydate = datetime.datetime.now()

print("__str__() string: ", mydate.__str__())
print("str() string: ", str(mydate))

print("__repr__() string: ", mydate.__repr__())
print("repr() string: ", repr(mydate))
