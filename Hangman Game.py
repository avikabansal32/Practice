#Hangman Game 
import random

print("---Welcome to Hangman Game!---")
words = ["APPLE", "PILLOW","REMOTE", "LAPTOP", "BOTTLE",]
word = random.choice(words)
lives = 6
guessed_letters = []

display = ['_'] * len(word)

while lives > 0:
    print("Current word: ", ' '.join(display))
    input_letter = input("Guess a letter: ").upper()

    if len(input_letter) != 1 or not input_letter.isalpha():
         print("Please enter a single alphabet letter.")
         continue

    if input_letter in guessed_letters:
        print(f"You have already guessed {input_letter}.")
        continue
    guessed_letters.append(input_letter)

    if input_letter in word:
        print(f"Good guess! {input_letter} is in the word.")
        for i in range(len(word)):
            if word[i] == input_letter:
                display[i] = input_letter         

    elif input_letter not in word:
        lives -= 1
        print(f"Sorry, {input_letter} is not in the word.")
        
    
    print(f"You have {lives} lives left.")
    print("Your guessed letters are: ", guessed_letters)

    if "_" not in display:
        print("Congratulations! You guessed the word.")
        break
    
if lives == 0:
    print(f"You ran out of lives. The word was: {word}. Better luck next time!")