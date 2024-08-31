import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    
    while True:
        # Prompt the user to enter their guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Compare the guess to the generated number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            print(f"It took you {attempts} attempts to guess the correct number.")
            break

if __name__ == "__main__":
    guessing_game()
