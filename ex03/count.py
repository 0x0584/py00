#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#									       #
#							  :::	   ::::::::    #
#    exec.py						:+:	 :+:	:+:    #
#						      +:+ +:+	      +:+      #
#    By: 0x0584 <archid-@1337.student.ma>	    +#+	 +:+	   +#+	       #
#						  +#+#+#+#+#+	+#+	       #
#    Created: 2023/02/18 21:21:35 by 0x0584	       #+#    #+#	       #
#    Updated: 2023/02/19 01:28:01 by 0x0584           ###   ########.fr        #
#									       #
# **************************************************************************** #
from sys import argv

def text_analyzer(s: str = None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """

    if s is None:
        s = input("");

    assert type(s) == str, "argument is not a string"

    uc_count: int = 0
    lc_count: int = 0
    sp_count: int = 0
    punct_count: int = 0

    for c in s:
        if c.isupper():
            uc_count += 1
        elif c.islower():
            lc_count += 1
        elif c.isspace():
            sp_count += 1
        else:
            punct_count += 1

    print("The text contains {} character(s):".format(len(s)))
    print("- {} upper letter(s)".format(uc_count))
    print("- {} lower letter(s)".format(lc_count))
    print("- {} punctuation mark(s)".format(punct_count))
    print("- {} space(s)".format(sp_count))

argc: int = len(argv)
assert argc == 2, "more than one argument was provided"
if __name__ == '__main__':
    text_analyzer(argv[1])
