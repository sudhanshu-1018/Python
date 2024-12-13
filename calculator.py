

print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.exit")
while True:
      choice = input("choose the number: (1/2/3/4/5)")
      if choice in ("1","2","3","4"):    
      
        num1 = float(input("write the 1st number: "))
        num2 = float(input("write the 2nd number: "))
        if choice == "1":
          print(num1 + num2)
        elif choice == "2":
          print(num1 - num2)
        elif choice == "3":
          print(num1 * num2)
        elif choice == "4":
              if num2 != 0:
                print(num1 / num2)
              else:
                print("Cannot divide by zero. Please enter a non-zero number for the 2nd number.")

      elif choice == '5':
              print("Exiting the calculator. Goodbye!")
              break
      else:
              print("Invalid input. Please enter a valid option.")




                         # 2nd dictionary


print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("'press any no. to exit except 1-4'")
while True:
    choice = input("choose the number: (1/2/3/4/)")
    if choice <="0" or choice >="5":
      
        print("Exiting the calculator. Goodbye!")
        break
    
    num1 = float(input("write the 1st number: "))
    num2 = float(input("write the 2nd number: "))
    if choice == "1":
        print(num1 + num2)
    elif choice == "2":
        print(num1 - num2)
    elif choice == "3":
        print(num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero. Please enter a non-zero number for the 2nd number.")





# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break

    else:
        print("Invalid Input")