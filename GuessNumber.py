import random


answar = random.randint(1, 99)

guess = input('what is your guess? ')
guess = int(guess)

while guess != answar:
    if guess > answar:
        print('mine is smaller!')
    else:
        print('mine is larger!')
    guess = input('what is your guess? ')
    guess = int(guess)

print('----------------\nwow! you did it! you rock!')
