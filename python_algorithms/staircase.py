#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    countSpace = n-1
    for i in range(1, n+1):
        print(" " * countSpace + "#" * i)
        countSpace = countSpace - 1


if __name__ == "__main__":
    n = int(input())
    staircase(n)