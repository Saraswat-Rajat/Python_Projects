# Functions with outputs
# the outputs of the function are outputed with return keyword

def format_name(first_name, last_name):

    if first_name == "" or last_name == "":
        return
    first_name = first_name.title()
    last_name = last_name.title()
    return (f"{first_name} and {last_name}")
# any logic after the return keyword in the function will not work


print(format_name(input("what is your first name? "),
      input("what is your last name? ")))


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]


year = int(input())
month = int(input())

days = days_in_month(year, month)
print(days)
