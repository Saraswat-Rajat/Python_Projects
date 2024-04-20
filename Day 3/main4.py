height = int(input("enter your height in cm : "))
bill = 0

if height >= 120:
    print("you can ride the rollercoster")

    age = int(input("Enter your age "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7")
    else:
        bill = 12
        print("adult tickets are $12")

    wants_pic = input("do you want a picture? y , n ")
    if wants_pic == "y":
        bill += 3
        print(f"you have to pay {bill} $")
    else:
        print(f"your bill is {bill}")
else:
    print("you cannot ride")
