import random
foo = [1, 2, 3, 4, 5]
print(random.choice(foo))

import random
bar = {6, 7, 8, 9, 10}
print(random.choice(list(bar)))

import random
print(random.randrange(1, 11)) # prints a random number from 1 to 10
print(random.randrange(1, 11, 2)) # prints a random odd number from 1 to 10

import random
foo = [1, 2, 3, 4, 5]
print(random.sample(foo, 2)) # prints a list of two random numbers from foo

import random
words = ["apple", "banana", "cherry", "date", "elderberry"]
word = random.choice(words)
print(word)






import random
import string

# Choose a random element from the string.ascii_letters constant, which contains both lowercase and uppercase letters
letter = random.choice (string.ascii_letters)

# Print the letter
print (letter)


import random
import string

# Choose a random element from the string.ascii_letters constant, which contains both lowercase and uppercase letters
letter = random.choice (string.ascii_letters)

# Print the letter
print (letter)