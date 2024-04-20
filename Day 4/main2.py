# lists

import random
fruits = ["apple", "pear", "cherry", "banana"]

print(fruits[0])
print(fruits[-1])
print(fruits[-3])

fruits[0] = "house"
print(fruits)


fruits.append("pomogranate")
print(fruits)


name_string = "angela, loope, ploty, loan, fsaf"

names = name_string.split(", ")
print(names)


num_items = len(names)

choice = random.randint(0, num_items - 1)

person = names[choice]
print(f"the person who will pay is {person}")
