#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/19 05:01:35 by 0x0584           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv

argc = len(argv)
assert argc <= 3, "too many arguments"

kata_max_width = 42
kata = argv[1] if argc == 2 else "The right format"
assert len(kata) <= kata_max_width, "kata too long"

kata_separator = argv[2] if argc == 3 else '-'
if __name__ == '__main__':
    print(kata.rjust(kata_max_width, kata_separator), end='')
