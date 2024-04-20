import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']

num1 = int(input("enter the number of letters :  \n"))
num2 = int(input("enter the number of numbres : \n"))
num3 = int(input("enter the number of symbols : \n"))

password = ""

for char in range(1, num1 + 1):
    random_char = random.choice(letters)
    password += random_char

for a in range(1, num2 + 1):
    random_char2 = random.choice(numbers)
    password += random_char2

for c in range(1, num3 + 1):
    random_char3 = random.choice(symbols)
    password += random_char3

print(password)
