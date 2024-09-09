import random
n= random.randint(1,100)
a = -1  # Initialize variable 'a' with a value that is not equal to 'n'
guesses = 1  # Initialize the number of guesses to 1
while(a != n):
    a = int(input("Guess the number: "))
    # Check if the user's guess is higher than the target number
    if(a>n):
        print("Lower number please")
        guesses +=1  # Increment the number of guesses
        # Check if the user's guess is lower than the target number
    elif(a<n):
        print("Higher number please")
        guesses +=1    # Increment the number of guesses
print(f"You have guessed the number {n} correctly in {guesses} attempts")