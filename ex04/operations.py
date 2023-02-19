#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/19 01:48:52 by 0x0584           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv

def ascii_to_integer(s: str):
    try:
        return int(s)
    except ValueError:
        assert False, "only integers"
        
if __name__ == '__main__':
    argc: int = len(argv)
    if argc != 1:
        assert argc == 3, "too many arguments"
    else:
        print("Usage: python {} <number1> <number2>\nExample:\n\tpython {} 14 12"
              .format(argv[0], argv[0]))
        exit()
    a: int = ascii_to_integer(argv[1])
    b: int = ascii_to_integer(argv[2])
    print("Sum:\t{}".format(a + b))
    print("Difference:\t{}".format(a - b))
    print("Product:\t{}".format(a * b))
    if b != 0:
        print("Quotient:\t{}".format(a / b))
        print("Remainder:\t{}".format(a % b))
    else:
        print("Quotient:\tERROR (division by zero)")
        print("Quotient:\tERROR (modulo by zero)")
