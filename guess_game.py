"""

This a guess game that allows the user to guess the random number in 5 tries.

"""
# Import randrange 
from random import randrange

# Generate random number between 0 and 100
random_number =  randrange(0, 101)

# Receive first guess from User
user_guess = (input('Type a number between 0 and 100: \n'))

if user_guess.isdigit():
    
    # Initialise count, guess_min and guess_max
    user_guess = int(user_guess)
    count = 1
    guess_min = 0
    guess_max = 100

    while count <= 5:
        if user_guess == random_number:
            print('                                             ')
            print('*********************************************')
            print(f'Congratulations!!! You guessed the random number {random_number} correctly in {count} attempt(s). Game over.')
            print('                                             ')
            break
        elif user_guess > random_number:
            guess_max = user_guess
            print(f'Wrong guess. Random number is between {guess_min} and {guess_max}')
        else:
            guess_min = user_guess
            print(f'Wrong guess. Random number is between {guess_min} and {guess_max}')

        if count == 5:
            print(f'Game over! You have exhausted your total attempts. Correct answer is {random_number}')
            break
        else:
            print(f'You have guessed {count} times, you have {5 - count} more attempts.')
            user_guess = (input('Try again: \n'))
            if user_guess.isdigit():
                user_guess = int(user_guess)
                count += 1
            else:
                print("Please type a number next time. Game Over!!!")
                quit()
else:
    print("Please type a number next time. Game Over!!!")
    quit()

