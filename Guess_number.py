# guessing_game.py
import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    while True:
        try:
            # Ask the player to guess the number
            guess = int(input("Enter your guess (1-100): "))

            # Increment the number of attempts
            attempts += 1

            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop when the guess is correct

        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    guessing_game()

