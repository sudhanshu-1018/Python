class employee:
    company_name="Apple"
    no_of_employee=0
    def __init__(self,name) -> None:
        self.name=name
        self.raise_amount=0.02
        employee.no_of_employee+=1

    def showdetails(self):
        print(f"the name of the employee is {self.name} and the raise amount in {self.no_of_employee} sized {self.company_name} is {self.raise_amount}")




a=employee.company_name="Google"
print(employee.company_name)


emp1=employee("sudhanshu")
emp1.raise_amount=0.3
# emp1.company_name="Apple India"
emp1.showdetails()


emp2=employee("rohan")
emp2.company_name="Nestle"
emp2.showdetails()