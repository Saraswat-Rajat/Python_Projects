# if else conditions

height = int(input("Enter the height in cm "))
gender = input("enter m or f: ")
if height >= 120:
    if gender == 'm':
        print("you can ride")
    else:
        print("you cannot ride")
elif height < 120:
    print("you cannot ride")


num = int(input("enter the number "))

if num % 2 == 0:
    print("num is even")
else:
    print("number is odd")
