# Welcome message
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# First decision: Left or Right
direction = input("You find yourself on a mysterious island. Do you want to go left or right? ").lower()

# Left path
if direction == "left":
    # Second decision: Swim or Wait
    action = input("You come across a river. Do you want to swim across or wait for a boat? ").lower()
    
    # Waiting path
    if action == "wait":
        # Third decision: Choose a door
        door_color = input("You reach the other side and find three doors. One red, one blue, and one yellow. Which color door do you choose? ").lower()

        # Outcome based on door color
        if door_color == "yellow":
            print("Congratulations! You found the treasure! You are now rich beyond your wildest dreams. You Win!")
        elif door_color == "blue":
            print("You open the blue door and are greeted by a hungry lion. Game over!")
        elif door_color == "red":
            print("As you open the red door, a trapdoor opens beneath you. You fall into a pit. Game over!")
        else:
            print("You hesitated and got caught by the island's guardians. Game over!")

    # Swimming path
    else:
        print("You decide to swim across the river, but you get caught in a strong current. Game over!")

# Right path
else:
    print("You venture into the dense forest, but you get lost and encounter dangerous wild animals. Game over.")
