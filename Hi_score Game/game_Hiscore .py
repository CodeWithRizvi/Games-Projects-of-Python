import random   # Import the random module to generate random numbers

def game():  
    # Print a message indicating the game is starting
    print("You are playiny the game...")
    # Generate a random score between 1 and 100
    score = random.randint(1,100)
    # Open the "hiscore.txt" file in read mode
    with open("hiscore.txt")as f:
        # Read the content of the file
        hiscore = f.read()
        # Check if the file is not empty
        if(hiscore!=""):
            # Convert the content to an integer
            hiscore = int(hiscore)

        else:
            # If the file is empty, set hiscore to 0
            hiscore = 0
            # Print the current score
    print(f"Your score: {score}")
    # Compare the current score with the high score
    if(score>hiscore):
        # If the current score is higher, update the high score
        # Open the file in write mode
        with open("hiscore.txt", "w") as f:
            # Write the new high score to the file
            f.write(str(score))
     # Return the current score
    return score
game()
