Letter = input()

GuessLetter = 0

while  GuessLetter < 5:
    print('Guess a Letter between A and Z:')
    guess = input()
    guess = guess

    GuessLetter = GuessLetter + 1

    if guess == Letter:
        break

if guess == Letter:
    print('You guessed the Letter in ' + str(GuessLetter) + ' tries!')
    print('True')

else:
    print('You did not guess the Letter. The Letter was ' + Letter)
    print('False')