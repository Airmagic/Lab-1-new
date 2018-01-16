#code is from example from the board that Clara James had up
# Importing random so can use it to get a number
import random

# stateing the program name
print('Random Guess')

# making a random number inside of a range
number = random.randint(1,11)

# asking for the guess from the user
guessedNumber = int(input('Guess the random number '))

# while loop to put out feed back for the user
while guessedNumber != number:
    if guessedNumber > number:
        print ('Number is lower than your guess')
    if guessedNumber < number:
        print ('Number is higher than your guess')
    # asking for another guess to find the number
    guessedNumber = int(input('Guess again for the number '))

# if it is a correct answer it doesn't activate the while loop
print('You guessed the random number')
