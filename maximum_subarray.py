import math

def find_max_subarray_brute(arr):
    left, right = 0, 0
    sum = -math.inf
    for l in range(0, len(arr)):
        s = 0
        for r in range(l, len(arr)):
            s += arr[r]
            if s > sum:
                sum = s
                left = l
                right = r
    return (left, right, sum)

def find_max_subarray_dnc(arr):
    low = 0
    high = len(arr) - 1
    return _find_max_subarray_dnc_helper(arr, low, high)

def _find_max_subarray_dnc_helper(arr, low, high):
    if high == low:
        return (low, high, arr[low])
    elif len(arr) <= 42:
        return find_max_subarray_brute(arr)
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = _find_max_subarray_dnc_helper(arr, low, mid)
        (right_low, right_high, right_sum) = _find_max_subarray_dnc_helper(arr, mid + 1, high)
        (cross_low, cross_high, cross_sum) = _find_max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

def _find_max_crossing_subarray(arr, low, mid, high):
    left_sum = -math.inf
    max_left = 0
    sum = 0
    for l in range(mid, low - 1, -1):
        sum += arr[l]
        if sum > left_sum:
            left_sum = sum
            max_left = l

    right_sum = -math.inf
    max_right = 0
    sum = 0
    for r in range(mid + 1, high + 1):
        sum += arr[r]
        if sum > right_sum:
            right_sum = sum
            max_right = r

    return (max_left, max_right, left_sum + right_sum)

def find_max_subarray_linear(arr):
    low, high = 0, 0
    sum = -math.inf
    l = 0
    s = 0
    for r in range(len(arr)):
        s += arr[r] # computes sum of arr[0..r] but computes just arr[r] when arr[0..r-1] is negative
        if s > sum:
            sum = s
            low, high = l, r
        if s < 0:
            s = 0
            l = r + 1
    return low, high, sum


# arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
#
# print(find_max_subarray_linear(arr))

# from datetime import datetime
#
# startTime = datetime.now().microsecond
# find_max_subarray_brute(arr)
# print(datetime.now().microsecond - startTime)
#
# pew = datetime.now().microsecond
# find_max_subarray_dnc(arr)
# print(datetime.now().microsecond - pew)

# n0 = 42
import timeit
# print(timeit.timeit('find_max_subarray_brute(arr)','from __main__ import find_max_subarray_brute\nfrom __main__ import arr', number=100))
# print(timeit.timeit('find_max_subarray_dnc(arr)','from __main__ import find_max_subarray_dnc\nfrom __main__ import arr', number=100))

for i in range (1, 101):
    print(i)
    print(timeit.timeit('find_max_subarray_brute(arr)',
                        'from __main__ import find_max_subarray_brute\narr = [2] * {}'.format(str(i)), number=1000))
    print(timeit.timeit('find_max_subarray_dnc(arr)',
                        'from __main__ import find_max_subarray_dnc\narr = [2] * {}'.format(str(i)), number=1000))
    print(timeit.timeit('find_max_subarray_linear(arr)',
                        'from __main__ import find_max_subarray_linear\narr = [2] * {}'.format(str(i)), number=1000))
    print()
