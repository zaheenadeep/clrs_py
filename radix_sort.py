from typing import List, NoReturn

def digit(num, i):
    return num // 10**i % 10

def radix_sort(arr: List[int], digit_count) -> NoReturn:
        for i in range(digit_count):
            counts = [0] * 10
            for j, num in enumerate(arr):
                counts[digit(num, i)] += 1

            for j, count in enumerate(counts):
                if j != 0:
                    counts[j] += counts[j - 1]

            sorted_arr = [0] * len(arr)
            for j in range(len(arr) - 1, -1, -1):
                sorted_arr[counts[digit(arr[j], i)] - 1] = arr[j]
                counts[digit(arr[j], i)] -= 1
            arr[:] = sorted_arr

if __name__ == '__main__':
    array = [6, 3, 567, 9, 3, 2, 46, 7, 3]
    radix_sort(array, 3)
    print(array)
