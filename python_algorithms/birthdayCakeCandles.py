#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    arrayMax = max(ar)
    count = 0
    for i in range(len(ar)):
        if ar[i] == arrayMax:
            count = count + 1
    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
