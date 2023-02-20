#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/20 12:06:51 by archid            #+#    #+#              #
#    Updated: 2023/02/21 23:30:03 by archid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv, stderr
from random import randint

def panic(err: str, err_code: int = 1):
    print(err, file=stderr)
    exit(err_code)

if __name__ == '__main__':
    argc = len(argv)
    num_min, num_max = (1, 99)
    if argc == 3:
        try:
            num_min, num_max = int(argv[1]), int(argv[2])
            assert num_max > num_min
        except ValueError:
            assert False, "arguments should be numbers"
    target = int(randint(num_min, num_max))

    print(
        "This is an interactive guessing game!\n"
        "You have to enter a number between {} and {} "
        "to find out the secret number.\n"
        "Type `exit' to end the game.\n"
        "Good luck!\n".format(num_min, num_max)
    )

    counter = 0
    while True:
        counter += 1

        try:
            n = int(input("What's your guess between {} and {}?\n>> "
                          .format(num_min, num_max)))
        except EOFError:
            panic("Good bye!", 1)
        except (ValueError, TypeError):
            n = None
            print("That was not a number!\nPlease retry\n")

        if n == None:
            counter -= 1
        elif n == target:
            break
        else:
            print('Too ' + ('high' if n > target else 'low') + '!')
    print(
        "Congratulations, you've got it!\n"
        "You won in {} attempt(s)!".format(counter)
    )
