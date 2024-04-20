# prime number checker

num = int(input("Enter the number : "))

isPrime = True

for t in range(2, num):

    if num % t == 0:
        isPrime = False


if isPrime == False:
    print("the number is not prime")
else:
    print("the number is prime")
