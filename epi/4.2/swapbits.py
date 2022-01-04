def swapbits(x, i, j):
    if ((x >> i) & 1) != ((x >> j) & 1): # different bits
        mask = (1 < i) | (1 < j)
        x ^= mask # swap
    return x

print(swapbits(739999999999999, 363, 343434))