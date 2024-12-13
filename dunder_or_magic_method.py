# from typing import Any


# class empoyee:
#     name="sudhanshu"
#     def __len__(self):
#         i=0
#         for c in self.name:
#             i=i+1
#         return i
    
# e=empoyee()
# print(e.name)
# print(e.__len__)
# print(len(e))


# __init__ take name, id etc from user by class

# __init__ method (also called CONSTRUCTOR)
#e.employee()   automatically call __init__
class box:
    def __str__(self) -> str:
        return f"The name of the box is {self.name}"
    
    def __repr__(self) -> str:
        return f"box('{self.name}')"
    
    def __call__(self):
        print("hey i am good")

