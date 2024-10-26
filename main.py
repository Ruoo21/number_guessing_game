import random
import time

high_score = 0
print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
)
print("You have 5 chances to guess the correct number.\n")

print("Please select the difficulty level: ")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)\n")
while True:
    guess_count = 0
    number_to_guess = random.randrange(1, 100)
    won = False
    while True:
        try:
            difficulty_level = int(input("Enter your choice: "))
        except ValueError:
            print("Please make sure your choice is 1, 2, or 3.")
            continue
        else:
            if difficulty_level > 3 or difficulty_level == 0:
                print("Please make sure your choice is 1, 2, or 3.")
                continue
            else:
                break

    match difficulty_level:
        case 1:
            print(
                "Great! You have selected the Easy difficulty level.\nLet's start the game!\n"
            )
            chances = 10
        case 2:
            print(
                "Great! You have selected the Medium difficulty level.\nLet's start the game!\n"
            )
            chances = 5
        case 3:
            print(
                "Great! You have selected the Hard difficulty level.\nLet's start the game!\n"
            )
            chances = 3

    start_time = time.time()
    while guess_count < chances:

        guess = int(input("Enter your guess: "))
        if guess > number_to_guess:
            print(f"Incorrect! The number is less than {guess}.")
            guess_count += 1
            continue
        elif guess < number_to_guess:
            print(f"Incorrect! The number is greater than {guess}.")
            guess_count += 1
            continue
        else:
            guess_count += 1
            print(
                f"Congratulations! You guessed the correct number in {guess_count} attempts."
            )
            won = True
            if guess_count < high_score or high_score == 0:
                high_score = guess_count
            break

    end_time = time.time()
    elapsed_time = end_time - start_time
    if won == False:
        print(f"Your high score is {high_score}")
        play_again = input("Looks like you lost! Want to play again? (y/n) ").lower()
        if play_again == "y":
            continue
        else:
            break
    else:
        print(f"Your high score is {high_score}")
        play_again = input(
            f"Looks like you won! It took you {elapsed_time:.2f} seconds. Want to play again? (y/n) "
        ).lower()

        if play_again == "y":
            continue
        else:
            break
