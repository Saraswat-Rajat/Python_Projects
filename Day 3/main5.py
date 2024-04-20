print("get your pizza")

size = input("enter the size s m l : ")
paperoni = input("paperoni y / n : ")
cheese = input("cheese y / n : ")

bill = 0

if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25

if paperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if cheese == 'y':
    bill += 1

print(f'your total bill is ${bill}')
