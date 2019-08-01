"""
An English text needs to be encrypted using the following encryption scheme. 
First, the spaces are removed from the text. Let L be the length of this text. 
Then, characters are written into a grid, whose rows and columns have the following constraints:
[sqrt(L)] <= row <= column <= [sqrt(L)], where [x] is floor function and [x] is ceil function.
For example, the sentence 
s = if man was meant to stay on the ground god would have given us roots
, after removing spaces is 54 characters long. sqrt(54) is between 7 and 8, so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots

Ensure that rows * columns >= L
If multiple grids satisfy the above conditions choose the one with the minimum area, i.e. rows * columns

The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message to encode and print.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    cols = math.ceil(math.sqrt(len(s)))
    remainder = len(s) % cols
    if ((cols - 1) * cols) < len(s):
        rows = cols
    else:
        rows = cols - 1
    # print(cols)
    # print(s)
    output = ''
    for i in range(0, cols):
        for j in range(0, rows):
            # print("looking at row ", i, " and column ", j)
            # print("last row has # elements: ", remainder)
            if remainder != 0:
                if j == (rows - 1):
                    if (i + 1) > remainder:
                        pass
                    else:
                        output += s[(j * cols) + i]
                else:
                    output += s[(j * cols) + i]
            else:
                output += s[(j * cols) + i]
        output += ' '
    # print(output)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
