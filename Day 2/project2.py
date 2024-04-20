print("Welcome to the tip calculator")

total = float(input("What was the total bill? "))
percent = float(input("How much percent tip would you like to give? "))

tip = (percent / total) * 100

num = float(input("enter the number of people "))

final = round(tip / num, 2)

print(f"Each one has to pay {final} dollars")
