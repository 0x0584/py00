#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/20 19:55:18 by archid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv

kata = (19,42,21)

if __name__ == '__main__':
    print("The 3 numbers are: {}, {}. {}".format(*kata))
