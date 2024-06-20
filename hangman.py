import random

print("Welcome to Hangman!")

words = ["apple", "banana", "orange", "kiwi", "watermelon", "cherry", "guava", "peach", "mango","dragonfruit"]
tgt_word = random.choice(words)
# print(tgt_word)

tgt_spellings = list(tgt_word)
replaced_tgt_spelling = len(tgt_spellings) * '_'

chance = 6

while True:

    n_cnt = 0
    y_cnt = 0

    # print(f"Current word : {tgt_spellings}")
    print(f"Current word : {replaced_tgt_spelling}")
    print(f"Incorrect guesses remaining : {chance}")
    letter = input("Guessed letters: ").lower()

    for i, tgt_spelling in enumerate(tgt_spellings, start=0):
        if tgt_spelling == letter:
            y_cnt = y_cnt + 1
            replaced_tgt_spellings = list(replaced_tgt_spelling)
            replaced_tgt_spellings[i] = letter
            replaced_tgt_spelling = "".join(replaced_tgt_spellings)
        else:
            n_cnt = 0

    # print(f"y_cnt : {y_cnt}, n_cnt : {n_cnt}")
    if y_cnt > 0:
        # print("There is at least one matching letter")
        print(f"Good job! '{letter}' is in the word.")
    elif n_cnt == 0:
        # print("There is no matching letter")
        print(f"Sorry, '{letter}' is not in the word.")
        chance = chance - 1

    if chance > 0 and tgt_word == replaced_tgt_spelling:
        print(f"Congratulations! You guessed the word : {tgt_word}")
        break

    if chance == 0:
        print(f"Game over! The word was : {tgt_word}")
        break
