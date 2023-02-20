#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/20 19:52:28 by archid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

def ascii_to_integer(s: str):
    try:
        n: int = int(s)
        return n
    except ValueType:
        return None

if __name__ == '__main__':
    argc: int = len(argv)
    assert argc == 2, "more than one argument was provided"
    n = ascii_to_integer(argv[1]);
    assert n is not None, "argument is not an integer"
    if n == 0:
        print("I'm Zero.")
    elif n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
