import getpass


def game():
    number = list(getpass.getpass(
        'Welcome to \'Guess the number\'!\nUser 1 please enter the number: '))
    count = 1

    while True:
        guess = input(f'\n\nUser 2 Guess {len(number)} digit number: ')

        guess_list = list(guess)
        guess_result = []

        if(guess == 'reset'):
            guess_list.clear()
            return game()

        if(guess == 'exit'):
            return print('Bye!')
        if guess_list == number:
            print(
                f"\nConragulations! You found the number {guess} in {count} guessing! 👏 🥳 👏\n")
            ans = input('Do you want to play again?: ')
            if(ans == 'Yes'):
                number.clear()
                guess_list.clear()
                guess = ' '
                return game()
            else:
                print('Bye!')
                break
        print(f'\n{guess}:', end=" ")
        for digit in guess_list:
            if digit in number:
                guess_index = guess_list.index(digit)
                number_index = number.index(digit)
                if(guess_index == number_index):
                    guess_result.append('+')
                else:
                    guess_result.append('-')
        guess_result.sort()
        if(len(guess_result) > 0):
            for i in guess_result:
                print(i, end=" ")
        else:
            print('0')
        count += 1


game()
