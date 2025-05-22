import random
import hangman_assets

def print_hangstage() :
    print(hangman_assets.hangman_stages[current_hangman_stage])
    print("Word: ", ''.join(hidden_word))
    print('')

def get_string(prompt) :
    while True:
        user_inp = input(prompt).lower()
        if user_inp.isalpha():
            return user_inp
        else:
            print("Invalid input. Enter a word or letter")


comp_word = random.choice(hangman_assets.words_list)

hidden_word = ['_'] * len(comp_word)

current_hangman_stage = 0

print("----------------------------------------------")
print("              WELCOME TO HANGMAN              ")
print("----------------------------------------------")

print(comp_word)

print_hangstage()

while True:
    user_guess = get_string("Guess a letter or the word: ")

    if 1 < len(user_guess):
        if user_guess == comp_word:
            print("You've successfully guessed the word!!!")
            break
        else:
            print("Not the word. Try again")

    else:
        if user_guess in comp_word:
            for index, letter in enumerate(comp_word):
                if letter == user_guess:
                    hidden_word[index] = user_guess
            print("You have guessed a letter!")
            
        else:
            print("Wrong guess!")
            current_hangman_stage += 1

    if current_hangman_stage + 2 < len(hangman_assets.hangman_stages):
        print_hangstage()
    else:
        current_hangman_stage += 1
        print("You loose. You've exhausted all your guesses!")
        print_hangstage()
        print(f"The word was '{comp_word}'")
        break
    
    
    if '_' not in hidden_word:
       print("You've successfully guessed the word!!!")
       break

