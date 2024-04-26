# modifying global scope

enemies = 2


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside the function{enemies}")

# global constants are useful
# naming convention is to use upper case
PI = 3.14159
URL = "https/google.com"
TWITTER_HANDLE = "@yu_angela"
