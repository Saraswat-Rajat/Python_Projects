# fizz buzz game

for n in range(1, 1001):
    if (n % 3 == 0 and n % 5 == 0):
        print("fizzbuzz")
    if (n % 3 == 0):
        print("fizz")
    if (n % 5 == 0):
        print("buzz")
    else:
        print(n)
