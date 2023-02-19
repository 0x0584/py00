#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/18 23:12:55 by 0x0584           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv
from typing import List
import numpy as np

def arr_to_str(arr: List[str]):
    return ''.join(arr)

if __name__ == '__main__':
    argc: int = len(argv)
    assert argc == 2
    reversed_str = arr_to_str(np.flipud([c for c in argv[1]]))
    print(arr_to_str([c.upper() if c.islower() else c.lower() for c in reversed_str]))
