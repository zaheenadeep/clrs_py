import random


def _partition(arr, p, r):
    key = arr[r]
    i = p - 1
    for j in range(len(arr) - 1):
        if arr[j] <= key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1


def _randomized_partition(arr, p, r):
    i = random.randint(0, len(arr)-1)
    arr[i], arr[r] = arr[r], arr[i]
    return _partition(arr, p, r)


def _quickselect_helper(arr, p, r, i):
    if p == r:
        return arr[p]
    q = _randomized_partition(arr, p, r)
    k = q - p
    if k == i - 1:
        return arr[q]
    elif k < i - 1:
        return _quickselect_helper(arr, p, q-1, i)
    else:
        return _quickselect_helper(arr, q+1, r, i-k-1)


def quickselect(arr, i):
    if i < 1 or i > len(arr):
        raise LookupError
    return _quickselect_helper(arr, 0, len(arr) - 1, i)


if __name__ == '__main__':
    arr = [7, 4, 2, 5, 6, 2, 1, 5, 54]
    print(quickselect(arr, 6))  # 2
    print(quickselect(arr, 45))  # Error
