def counting_sort(arr, largest):
    sorted_arr = [0] * len(arr)

    counts = [0] * (largest+1)
    for integer in arr:
        counts[integer] += 1
    for i, count in enumerate(counts):
        if i != 0:
            counts[i] += counts[i-1]

    for integer in arr:
        sorted_arr[counts[integer] - 1] = integer
        counts[integer] -= 1

    return sorted_arr

if __name__ == "__main__":
    arr = [35, 31, 14, 33, 42, 10, 14, 19, 27, 44, 31, 26, 31]
    print(counting_sort(arr, max(arr)))

