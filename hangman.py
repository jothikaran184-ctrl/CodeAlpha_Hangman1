import random

def play_hangman():
    # Small list of 5 predefined words
    words = ["python", "code", "alpha", "intern", "game"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("=== Welcome to Hangman ===")
    
    while incorrect_guesses < max_incorrect:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])
        print(f"\nWord: {display_word}")
        
        if display_word == word_to_guess:
            print("Congratulations! You guessed the word correctly!")
            return
            
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabetical letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect - incorrect_guesses} guesses left.")
            
    print(f"\nGame Over! The hidden word was '{word_to_guess}'.")

if __name__ == "__main__":
    play_hangman()