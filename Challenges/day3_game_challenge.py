print( "Welcome to Treasure Island\nYour mission is to find the Treasure")
left = "l"
right = "r"
direction = input(f" You can go left or right. Type {left} for left or {right} for right\n").lower()

if direction != left and direction != right:
 print("game over")

if direction == right:
    print("you fall into a hole!\nGame over!")
elif direction == left:
    swim_wait = input("Do you want to swim or wait? Type S for swim or W for wait\n").lower()
   
    if swim_wait == "s":
        print("Bugger! You got eaten by a shark!!")
    elif swim_wait =="w":
        which_door = input("Choose a door B for blur door, R for red door and Y for yellow door\n").lower()
        if which_door =="b":
            print("You have been eaten by beasts! Game Over!")
        elif which_door == "r":
            print("Youve been burned by fire! Game over!")

        elif which_door =="y":
            print( "congratulations you Win")

        else:
            print("You chose a door other than listed!..Game over") # any other input thats not whats asked for




