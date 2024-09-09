import random   # Import the random module to generate random numbers
"""
1 for snake
-1 for water
0 for gun
"""
# Randomly select a choice for the computer. This will be either -1, 0, or 1.
computer = random.choice([-1,0,1])
# Take user input for their choice
yourstr= input("Enter your chuice: ")
# Create a dictionary to map user input to the corresponding choice value.
# 's' maps to 1 (Snake), 'w' maps to -1 (Water), 'g' maps to 0 (Gun)
yourDict={"s":1,"w":-1,"g":0}
# Create a dictionary to map choice values to their names.
# This is used to display the choices to the user.
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
# Use the dictionary to convert the user's input to the corresponding choice value.
you = yourDict[yourstr]
# Display the choices made by the user and the computer.
# Use reverseDict to convert the choice values back to their names for a user-friendly display.
print(f"Your choise {reverseDict[you]}\nComputer choise {reverseDict[computer]}")

if (computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    else:
        print("Something went worng!")
    