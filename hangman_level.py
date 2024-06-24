import random

print("Welcome to Hangman!")

level = input("Choose the level (1,2,3): ")
words= []
chance = 6

if level == '1':
    print(f"level{level} : Color")
    words = ["black", "pink", "purple", "red", "blue", "green", "grey", "yellow", "white", "ivory"]
elif level == '2':
    print(f"level{level} : Fruit")
    words = ["apple", "banana", "orange", "kiwi", "watermelon", "cherry", "guava", "peach", "mango", "dragonfruit"]
elif level == '3':
    print(f"level{level} : Animal")
    words = ["elephant", "panda", "alligator", "squirrel", "hippo", "capybara", "koala", "tiger", "deer", "monkey"]
else:
    level = '1'
    print(f"Wrong level! Start from level{level} : Color")
    words = ["black", "pink", "purple", "red", "blue", "green", "grey", "yellow", "white", "ivory"]

tgt_word = random.choice(words)

tgt_spellings = list(tgt_word)
replaced_tgt_spelling = len(tgt_spellings) * '_'

while True:

    n_cnt = 0
    y_cnt = 0

    print(f"Current word : {replaced_tgt_spelling}")
    print(f"Incorrect guesses remaining : {chance}")
    letter = input("Guessed letters: ")
    for i, tgt_spelling in enumerate(tgt_spellings, start=0):
        if tgt_spelling == letter:
            y_cnt = y_cnt + 1
            replaced_tgt_spellings = list(replaced_tgt_spelling)
            replaced_tgt_spellings[i] = letter
            replaced_tgt_spelling = "".join(replaced_tgt_spellings)
        else:
            n_cnt = 0

    if y_cnt > 0:
        print(f"Good job! '{letter}' is in the word.")
    elif n_cnt == 0:
        print(f"Sorry, '{letter}' is not in the word.")
        chance = chance - 1

    if chance > 0 and tgt_word == replaced_tgt_spelling:
        print(f"Congratulations! You guessed the word : {tgt_word}")
        break

    if chance == 0:
        print(f"Game over! The word was : {tgt_word}")
        break
