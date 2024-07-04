import random
lower_bound = 1
upper_bound = 1000
max_attempts = 10
secret_number = random.randint(lower_bound, upper_bound)
print("Welcome to game created by Lakshya ! ")
def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Wrong input. Please enter a number within the defined range !")
        except ValueError:
            print("Wrong input. Please enter a valid number !")

# taking  the user's guess
user_guess = get_guess()
attempts = 0
while attempts < max_attempts:
    attempts += 1
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        break
    elif user_guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")
    user_guess = get_guess()

if attempts == max_attempts:
    print(f"Out of attempts! The secret number was {secret_number}.")