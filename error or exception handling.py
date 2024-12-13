a=input("Enter the number:")
print(f"Multiplication table of {a} is:")
 
try:
  for i in range(1,11):
    print(f"{int(a)}x{i}={int(a)*i}")
except:
  print("invalid input")
# except Exception as e:
#   print(e)
print("SOME IMPORTANT lines:")

# Handaling Specific error
try:
  num=int(input("Enter an integer:"))
  a=[6,3]
  print(a[num])
except ValueError:
  print("Number Enter is not an integer.")
except IndexError:
  print("Index error")