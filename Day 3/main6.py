print("lets calculate your love score")

first = input("enter your name ")
second = input("enter your partners name ")

final = first + second
lower_name = final.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

first_digit = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

second_digit = l + o + v + e

score = int(str(first_digit + second_digit))

if (score < 10) or (score > 90):
    print(f'yopur score is {score} you are not meant to be together')
elif (score >= 10) and (score <= 50):
    print(f'your score is {score} , you are alright together')
else:
    print(f"your score is {score}, you are perfect together")
