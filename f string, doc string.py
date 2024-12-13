# string formatting

letter="hey I am {0} and I am from {1}"
country="india"
name="sudhanshu kumar singh"
print(letter.format(name,country))

txt="for only {price:.2f} dollars!"
print(txt.format (price=49.0999))


# f string 
print(f"hey I am {name} and  I am from {country}")

price=49.0999
print(f"for only {price:.2f} dollars!")

txt=f"for only {price:.2f} dollars!"
print(txt)

print(f"{2*5}")



# doc string
def square(n):
    '''takes n,return sqaure of n'''
    print(n**2)
square(5)

print(square.__doc__)