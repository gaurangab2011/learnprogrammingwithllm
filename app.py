import random

def guess_game():
    print("Welcome to the Guessing Game!")
    random_number = random.randint(1,10)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10:"))
            attempts += 1
            if guess < 1 or guess > 10:
                print("Your guess is out of range. Please try again.")
            elif guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")
            continue

if __name__ == "__main__":
    guess_game()