import random
import hangman_assets

def yesRno(prompt) :
    while True:
        user_inp = input(prompt).lower()
        if user_inp in ('y', 'n'):
            return user_inp
        else:
            print('invalid input')

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

guessed_letters = []

print("----------------------------------------------")
print("              WELCOME TO HANGMAN              ")
print("----------------------------------------------")


print_hangstage()

while True:
    user_guess = get_string("Guess a letter or the word: ")

    if user_guess in guessed_letters:
        print("You've already guessed this letter")
        continue

    guessed_letters.append(user_guess)

    if 1 < len(user_guess):
        if user_guess == comp_word:
            hidden_word = user_guess
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

    if current_hangman_stage < len(hangman_assets.hangman_stages) - 1:
        print_hangstage()
    else:
        print("You loose. You've exhausted all your guesses!")
        print_hangstage()
        print(f"The word was '{comp_word}'")
        user_exit = yesRno("continue? (y/n): ")
        if user_exit == 'n':
           break
    
    
    if '_' not in hidden_word:
       print("You've successfully guessed the word!!!")
       user_exit = yesRno("continue? (y/n): ")
       if user_exit == 'n':
           break

