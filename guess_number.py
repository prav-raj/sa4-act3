number = 10

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? Type 'q' to quit: ")

    if guess.lower() == 'q':
        print(f"The number was {number}. Goodbye!")
        break

    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print("Sorry! Try again.")

