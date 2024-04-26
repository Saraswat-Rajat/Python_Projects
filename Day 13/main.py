# 1. Describing the problem

from random import randint


def my_function():
    for i in range(1, 20):
        if i == 20:
            print("you got it")

    my_function()

# change 20 to 21 to run the code

# 2. Reproduce the bug


dice_img = ['1', '2', '3', '4', '5', '6']
dice_num = randint(1, 6)
print(dice_img[dice_num])

# change randint(1,5)


# 3.Play Computer

year = int(input("enter the year of birth"))

if year > 1980 and year < 1994:
    print("You are a millenial")
elif year > 1994:
    print("you are a gen Z")

# change >= 1994

# 4. fix red lines

# 5. print is your friend

pages = 0
word_per_page = 0

pages = int(input("enter no. of pages"))
word_per_page == int(input("enter no. of words per page"))

total_words = pages * word_per_page
print(total_words)


# add print(f"{pages}, {word_per_page}"")

# 5. use the debugger

# python tutor
# thonny
def mutate(a_list):
    b_list = []

    for item in a_list:
        new_item = item*2
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 4, 54, 643, 2])
