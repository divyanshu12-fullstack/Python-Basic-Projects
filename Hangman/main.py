import random
import string

from words import words


def create_question():
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()
    return word


def give_hint(word, used_letters):
    # Randomly select one or two letters from the word as a hint
    hint_letters = random.sample(set(word), k=2)  # `k=2` gives two hint letters
    used_letters.update(hint_letters)
    return used_letters


def hangman():
    word = create_question()  # Randomly select a word
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase)  # Legal letters (A-Z)
    used_letters = set()  # Keep track of guessed letters
    lives = 6  # Number of incorrect attempts allowed

    # Provide the user with an initial hint by revealing some letters
    used_letters = give_hint(word, used_letters)
    print(f"Here's your starting hint! Some letters are already revealed: {', '.join(used_letters)}")

    # Game loop
    while len(word_letters - used_letters) > 0 and lives > 0:
        # Show the player their used letters
        print("\nYou have", lives, "lives left and used these letters: ", ' '.join(sorted(used_letters)))

        # Show the current state of the word (guessed letters or '-' for guessed)
        box_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(box_list))

        # User input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Good guess!")
            else:
                lives -= 1  # Lose a life if the guess is wrong
                print("Incorrect guess!")

        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")

        else:
            print("Invalid input. Please enter a letter from A-Z.")

    # End of the game
    if lives == 0:
        print("You lost! The word was:", word)
    else:
        print("Congratulations! You guessed the word:", word)


hangman()
