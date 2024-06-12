secret_number = 9
attemted = 0

while attemted < 3:
    guess = input('guess: ')
    if int(guess) == secret_number:
        print('You win!')
        break
    attemted = attemted + 1
if attemted == 3:
    print('Sorry you failed')