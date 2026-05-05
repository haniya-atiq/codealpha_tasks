import random

def hangman():
    words = ["python", "apple", "chair", "tiger", "robot"]
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    display_word = ["_"] * len(word)

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            print("Wrong!")
            incorrect_guesses += 1

    # Game result
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

# Run the game
hangman()