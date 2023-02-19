#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/19 01:51:44 by 0x0584           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv

kata = (19,42,21)         # Put this at the top of your kata00.py file

if __name__ == '__main__':
    print("The 3 numbers are: {}, {}. {}".format(*kata))
    pass
