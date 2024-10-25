import random

print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
)
print("You have 5 chances to guess the correct number.\n")

print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")
while True:
    try:
        difficulty_level = int(input("Please select the difficulty level: "))
    except ValueError:
        print("Please make sure your choice is 1, 2, or 3.")
        continue
    else:
        if difficulty_level > 3 or difficulty_level == 0:
            print("Please make sure your choice is 1, 2, or 3.")
            continue
        else:
            break
