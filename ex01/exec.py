#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/21 23:29:33 by archid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
from typing import List
from numpy import flipud

def _str(arr: List[str]):
    return ''.join(arr)

if __name__ == '__main__':
    argv = flipud(argv)
    argv.pop()

    args = list()
    for arg in argv:
        words = list()
        for word in arg.split():
            reversed_str = _str(flipud([c for c in word]))
            words.append(_str([c.upper() if c.islower() else c.lower()
                               for c in reversed_str]))
        words = flipud(words)
        args.extend(words)

    for i, arg in enumerate(args):
        print(arg, end=' ' if i + 1 != len(args) else '\n')
