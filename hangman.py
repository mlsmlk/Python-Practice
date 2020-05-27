import getpass
'''
___________
|    |
|   ( )
|   /|\
|   / \
|___

'''


def hangman(live):
    if (live == 9):
        print('\n\n\n\n\n___')
    elif (live == 8):
        print('\n|\n|\n|\n|\n|___')
    elif (live == 7):
        print('___________\n|\n|\n|\n|\n|___')
    elif (live == 6):
        print('''
              ___________
              |    |
              |   
              |    
              |    
              |___''')
    elif (live == 5):
        print('''
            ___________
            |    |
            |   ( )
            |    
            |    
            |___''')
    elif (live == 4):
        print('''
            ___________
            |    |
            |   ( )
            |    |
            |    
            |___''')
    elif (live == 3):
        print('''
              ___________
              |    |
              |   ( )
              |   /|
              |    
              |___''')
    elif (live == 2):
        print('''
              ___________
              |    |
              |   ( )
              |   /|\ \t
              |    
              |___''')
    elif (live == 1):
        print('''
              ___________
              |    |
              |   ( )
              |   /|\ \t
              |   /
              |___''')
    else:
        print('''
            ___________
            |    |
            |   ( )
            |   /|\ \t
            |   / \ \t
            |___''')


def display(guessed):
    for i in guessed:
        print(i, end=' ')
    print('\n')


def game():
    copy = getpass.getpass('User 1 please enter the word: ')
    word = list(copy)
    guessed = list('_' * len(word))
    if ' ' in word:
        index = word.index(' ')
        guessed[index] = ' '
    guess_list = []
    live = 9

    print(f'Let\'s start!You have {live+1} lives!\n')
    display(guessed)

    while (True):
        guess = input('Guess letter: ')
        if(guess == 'reset'):
            guessed.clear()
            word = ''
            return game()

        if(guess == 'exit'):
            return print('Bye!')
        if guess in guess_list:
            guess = ''
            print('Already guessed!')

        elif guess in word:
            count = word.count(guess)
            for j in range(count):
                index = word.index(guess)
                guess_list.append(guess)
                guessed[index] = guess
                word[index] = '_'
            print('\n')
            display(guessed)
            print('Perfect! 🤩')

        else:
            hangman(live)
            guess_list.append(guess)
            display(guessed)
            if (live == 0):
                print(f'You lost!☹ ☹ ☹\n The word was "{copy}"')
                break
            print(f'Wrong guess! {live} lives left! Let\'s try again!')
            live -= 1

        if '_' not in guessed:
            print('Congratulations, you won!👏 🥳 👏')
            break

    if(input('\nDo you want to play again?: ') == 'Yes'):
        guessed.clear()
        word = ''
        return game()
    else:
        print('Bye!')


game()
