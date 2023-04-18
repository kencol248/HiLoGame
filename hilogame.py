# Kenyah Collins
# 11/8/2022
# collins-HiLoGame.py

# This program will have the user play the hi/low guessing game
# The program will pick a number between 1 and a max input value from user
# The user will be guessing the number until it matches the computers random 
# chosen number.

while True:
    import random

    while True:
    #user will set a max number for this game, use input statement, "What should be the max number for this game?"
        max_chosen_val = input('\nWhat should be the maximum number for this game? ')
        if max_chosen_val.isdigit():
            break
    #have computer generate chosen random number for user to guess
    computer_chosen_numb = random.randint(1, int(max_chosen_val))
    while True:
        #while True
        #Another input statement for user guessing comps number "Guess my number" and have a variable for user guess
        user_guess = int(input('Guess my number? '))

        while user_guess != computer_chosen_numb:
            #if user picks a number too high or low, computer lets user know
            if user_guess < computer_chosen_numb:
                print("That's too low! Guess again!")
                user_guess = int(input('Guess my number? '))
            elif user_guess > computer_chosen_numb:
                print("That's too high! Guess again!")
                user_guess = int(input('Guess my number? '))
        if user_guess == computer_chosen_numb:
            break
            
    #if user guesses correctly, computer will tell user they guessed correctly
    if user_guess == computer_chosen_numb:
        print('Good job! You guessed it!')

#Then comp will ask if user wants to play again, if no say "thanks for playing", if yes resart program
   
    again=input('Want to play again? (yes/no?) ')
    if again.lower() != 'yes':
        break

print('\nthanks for playing!')
