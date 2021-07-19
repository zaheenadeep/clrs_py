def _partition(arr, p, r):
    pass

def _randomized_partition(arr, p, r):
    pass

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
         return _quickselect_helper(arr, q+1, r,  )

def quickselect(arr, i):
    return _quickselect_helper(arr, 0, len(arr) - 1, i)