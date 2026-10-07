import random 

def check_guess(guess, secret_number):
    #This is for if, else and elif.
    if guess < secret_number:
     return "Sorry, your guess is too low...try again!"
    elif guess > secret_number:
     return "Nope, your guess is too high! Have another go..."
    else:
     return "You got it right, player! Well done!"



def game_start():
    secret_number = random.randint(1, 100)

    print("Hi there, player! Welcome to the Guessing Game!")
    print("The aim of this game is simple: guess what number I'm thinking of between 1 and 100! ")

    # TODO:

    attempts = 0
    #Loops: while, for, do...while
    while(True):
        guess = int(input("Write a number, any number:"))
        attempts = attempts + 1 
        hint = check_guess(guess, secret_number)
        print(hint)
        
        if hint == "You got it right, player! Well done!":
            print(f"You guessed {attempts} times! Good job!")
            break 
game_start()