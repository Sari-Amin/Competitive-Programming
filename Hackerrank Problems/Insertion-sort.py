#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    num = arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i] > num:
            arr[i + 1] = arr[i]
        else:
            arr[i + 1] = num
            break
        for j in arr:
            print(j,end=" ")
        print()
    if arr[0] > num:
        arr[0] = num
    for j in arr:
        print(j,end=" ")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
