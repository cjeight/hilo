from random import randint

number = number = randint(0, 100)
guess = 1
print('Welcome to the Hi - LO game.')
while guess > 0:

    guess = int(input('Guess a number between 1 & 100: '))

    if guess == number:
        print(f'Got it: The number is {number}')
        guess = 0
    elif guess > number:
        print('Too high!')
    elif guess < number:
        print('Too low!')

# end of file
