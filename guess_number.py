number = 10
tries = 5
print("I'm thinking of a number...")

while True:
    guess = input(f"What number am I thinking of? {tries} tries remaining. Type 'q' to quit: ")

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
        tries -= 1
    
    if tries == 0:
        print(f"You're out of tries! The number was {number}")
        break

