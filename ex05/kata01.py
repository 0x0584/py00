#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/20 19:55:33 by archid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if __name__ == '__main__':
    for lang in kata.keys():
        print("{} was cerated by {}".format(lang, kata[lang]))
