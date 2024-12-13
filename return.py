def my_function(x):
  return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def average(*number):
  print(type(number))
  #In the code sum=sum+i, sum is a variable that stores the total sum of all the numbers added together.
  # In each iteration of the loop, a new number i is added to the current value of sum.
  # This way, sum keeps track of the running total as the loop goes through each number.
  sum=0
  for i in number:
    sum=sum+i
  return sum/len(number)

c=average(2,5)
print(c)
