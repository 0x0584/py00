#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/19 02:38:51 by 0x0584           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv

kata = (2019, 9, 25, 3, 30) # Put this at the top of your kata02.py file

if __name__ == '__main__':
    year, day, month, hrs, mins = kata
    print("{:02}/{:02}/{:04} {:02}:{:02}".format(day, month, year, hrs, mins));
