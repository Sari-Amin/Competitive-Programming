#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ans = s[0].upper()
    for i in range(1,len(s)):
        if s[i-1] == " " and s[i].isalpha():
            ans += s[i].upper()
        else:
            ans += s[i]
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
