import random


def hangman(word):
    print("H A N G M A N")
    hidden_word = "-" * len(word)
    lives = 8
    already_input = []

    while True:
        if lives == 0:
            print("You are hanged!")
            break
        if hidden_word == word:
            print("You guessed the word!")
            print("You survived!")
            break

        print("")
        print(hidden_word)

        guess = input("Input a letter: > ")

        if guess in already_input:
            lives -= 1
            print("No improvements")

        if guess in word:
            word_input = ""
            for x in range(len(word)):
                if guess == str(word[x]):
                    word_input += guess
                    already_input.append(guess)
                else:
                    word_input += hidden_word[x]
            hidden_word = word_input
        else:
            print("No such letter in the word")
            lives -= 1


word_list = ["python", "java", "kotlin", "javascript"]
word = random.choice(word_list)
hangman(word)
