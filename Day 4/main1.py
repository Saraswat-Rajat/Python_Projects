# random module -> python uses the Morsenne twister algorithm to generate random numbers
# it is a type of pseudo random number generator

import my_module
import random
a = random.randint(1, 10)
print(a)


b = random.randint(1, 2)

if b == 1:
    print("heads")
else:
    print("tails")


print(my_module.pi)

# to get number between 0 and 1
random_float = random.random()
# to get numbers between 0 and 5
print(random_float * 5)


love_score = random.randint(1, 100)
print(love_score)
