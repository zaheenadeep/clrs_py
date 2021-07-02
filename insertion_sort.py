#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the insertionSort function below.
def insertionSort(arr):
    if len(arr) <= 1:
        return 0

    count = 0
    arrCopy = arr.copy()
    for j in range(1, len(arrCopy)):
        key = arrCopy[j]
        i = j - 1
        while i >= 0 and arrCopy[i] > key:
            arrCopy[i + 1] = arrCopy[i]
            i -= 1
        arrCopy[i + 1] = key
        count += (j - (i + 1))
    return count


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        print(str(result) + '\n')

