import random


def play_game(lower_bound, upper_bound):
    target_number = random.randint(lower_bound, upper_bound)
    guess = None
    attempts = 0
    max_attempts_for_hint = 5  # Number of attempts after which a hint is given

    print(f"Guess the number between {lower_bound} and {upper_bound}!")

    while guess != target_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Correct! The number was {target_number}.")
            print(f"You guessed it in {attempts} attempts.")

        if attempts == max_attempts_for_hint:
            if target_number % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")

    return attempts


def main():
    best_score = None
    play_again = True

    while play_again:
        print("Welcome to the Number Guessing Game!")

        # Setting the range of numbers
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))

        # Playing the game
        attempts = play_game(lower_bound, upper_bound)

        # Updating the best score
        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"New best score: {best_score} attempts!")

        # Asking if the user wants to play again
        play_again = (
            input("Do you want to play again? (yes/no): ").strip().lower() == "yes"
        )

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
