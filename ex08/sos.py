#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/20 12:06:51 by archid            #+#    #+#              #
#    Updated: 2023/02/20 20:05:11 by archid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

morse_table = dict(
    a=".-", b="-...", c="-.-.", d="-..", e=".",
    f="..-.", g="--.", h="....", i="..", j=".---",
    k="-.-", l=".-..", m="--", n="-.", o="---",
    p=".--.", q="--.-", r=".-.", s="...", t="-",
    u="..-", v="...-", w=".--", x="-..-", y="-.--",
    z="--..", _0="-----", _1=".----", _2="..---",
    _3="...--", _4="....-", _5=".....", _6="-....",
    _7="--...", _8="---..", _9="----.", sp='/'
)

def encode(tokens: str):
    global morse_table
    for i, token in enumerate(tokens):
        space = ' ' if i + 1 != len(tokens) else ''
        if token == ' ':
            print(morse_table.get('sp'), end=space)
        else:
            for c in token:
                if c.isalpha():
                    print(morse_table.get(c), end=space)
                else:
                    print(morse_table.get('_' + c), end=space)
    print('')

if __name__ == '__main__':
    argc = len(argv)
    tokens = list()
    for i in range(1, argc):
        words = argv[i].strip().lower().split()
        for i in range(len(words)):
            tokens.append(words[i])
            if i + 1 != len(words):
                tokens.append(' ')
    for token in tokens:
        if token != ' ':
            assert token.isalnum(), 'only alpha-numeric characters are allowed'
    encode(tokens)
