
class employee:
    company="Apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company

e1=employee()
e1.name="harry sir"
print(e1.company)
e1.show()
e1.change_company("Tesla")
print(e1.company)

e1.show()
print(employee.company)







# class employee:
#     company="Apple"
#     def __init__(self,name) -> None:
#         self.name=name

#     def show(self):
#         print(f"the name is {self.name} and company is {self.company}")

#     @classmethod
#     def change_company(cls,new_company):
#         cls.company=new_company

# e1=employee("rohan")
# # e1.name="harry"
# print(e1.company)
# e1.show()
# e1.change_company("Tesla")
# print(e1.company)

# e1.show()
# print(employee.company)
