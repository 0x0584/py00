#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/20 11:44:59 by 0x0584           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv

def panic(s: str, status: int=1):
    print(s)
    exit(status)

if __name__ == '__main__':
    argc = len(argv)
    if argc != 3:
        try:
            word_len = int(argv[2])
        except ValueError:
            panic("Error")
    print([s for s in ''.join([c for c in argv[1].trim()
                               if not c.isalphanum()]).split()
           if len(s) > word_len])
