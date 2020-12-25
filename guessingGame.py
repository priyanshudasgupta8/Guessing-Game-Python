import random

while True:
    intention = input('Do you want to play a guessing game (y/n)? ').lower()
    num = random.randint(1, 9)
    count = 0

    if intention == 'y':
        while count < 5:
            qwerty = int(input('Guess what number I chose (1-9): '))

            if (num == qwerty):
                print('Nice job! You guessed it in', count+1, 'guesses')
                break
            elif (num < qwerty):
                print('Almost there... Just a little bit lower')
            elif (num > qwerty):
                print('Almost there... Just a little bit higher')

            count += 1

        if count == 5:
            print('The number was', num)

        
    elif intention == 'n':
        print('Ok bye! Maybe you\'d want to play later')

