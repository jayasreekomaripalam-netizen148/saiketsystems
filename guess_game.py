import random

def guess_number_game():

    print("===== GUESS THE NUMBER GAME =====")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try a higher number.")

            elif guess > number:
                print("Too high! Try a lower number.")

            else:
                print("Congratulations! 🎉")
                print(f"You guessed the correct number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    guess_number_game()