print("welcome to the treasure island game")

direction = input("left or right? ")

if direction == "left":
    swim = input("swim or wait? ")
    if swim == "swim":
        print("Game Over")
    elif swim == "wait":
        door = input("Which door? red, blue or yellow?  ")

        if door == "red":
            print("Game over")
        if door == 'yellow':
            print("you won")
        if door == "blue":
            print("Game Over")

else:
    print("Game over")
