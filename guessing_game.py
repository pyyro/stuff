import random
name = input('What is your name?')

print('Well, ' + str(name) + " ,I'm thinking of a number between 1 and 20.")
randomNumber = random.randint(1, 20)
try:
    for guessesTaken in range(1, 7):
        print('Take a guess.')
        guess = int(input())

        if guess < randomNumber:
            print('Your guess is too low.')
        elif guess > randomNumber:
            print('Your guess is too high.')
        else:
            break  # Condition for correct guess.
    if guess == randomNumber:
        print('You got it!')
        print('Good job ' + str(name) + ', You guessed the number in ' + str(guessesTaken) + ' guesses.')
    else:
        print('Nope the number I was thinking of was ' + str(randomNumber))
except:
    print('You did not enter a number')
