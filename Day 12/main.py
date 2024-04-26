# scope -> this is the boundry where the variables can be accessed

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function {enemies}")


increase_enemies()
print(f"enemies outside function {enemies}")


# local scope ->

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
print(potion_strength)

# this will not print

# global scope ->

player_health = 10
# this is a global variable


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()

# global and local scope is applied to function, variable, anything you can name

# in python there is no block scope

game_level = 2
enemies2 = ["skeleton", "zombie", "alien"]


def create_enemy():
    if game_level < 5:
        new_enemy = enemies2[0]


print(new_enemy)
# this will not work as if we create a variable within a function that if can be accessed within that function
# if created in if block then it is not a local scope
