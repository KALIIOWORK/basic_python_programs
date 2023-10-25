import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        user_guess = input("Enter your guess: ")
        attempts += 1
        
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue

        user_guess = int(user_guess)
        
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! Congratulations, you guessed the number in {attempts} attempts!")
            break

if __name__ == "__main__":
    number_guessing_game()
    
