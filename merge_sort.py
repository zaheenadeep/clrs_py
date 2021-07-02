def merge_sort(arr, p, r):
    if p <= r:
        q = (p + r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    left = [arr[i] for i in range(p, q+1)]
    right = [arr[j] for j in range(q+1, r+1)]
    i = 0
    j = 0
    for k in range(p, r+1):
        if left[i] >= right[j]:
            arr[k] = right[j]
            j += 1
        else:
            arr[k] = left[i]
            i += 1

