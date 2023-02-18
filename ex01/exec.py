#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/18 23:02:37 by 0x0584           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv
import numpy as np

switch_case = lambda c: c.upper() if c.islower() else c.lower()
arr_to_str = lambda arr: ''.join(arr)

if __name__ == '__main__':
    argc = len(argv)
    assert argc == 2
    reversed_str = arr_to_str(np.flipud([c for c in argv[1]]))
    print(arr_to_str([switch_case(str(c)) for c in reversed_str]))
