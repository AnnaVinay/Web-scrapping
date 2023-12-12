import random
def number_guessing_game():
    target_number = random.randint(1,100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 to 100")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess ==target_number:
            print(f' Congratulation!! your guess number {user_guess} is correct')
            break
        elif user_guess < target_number:
            print("Too low. Try another number.")
        else:
            print("Too high. Try another value")

if __name__ == "__main__":
    number_guessing_game()
    