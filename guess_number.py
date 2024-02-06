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
        if int(guess) < number:
            print("Sorry, you're too low! Try again.")
        else:
            print("Sorry, you're too high! Try again.")

