def _set(x, bit, idx):
    if bit:
        return x | (1 << idx)
    else:
        return x & ~(1 << idx)

def swapbits(x, i, j):
    p = (x & (1 << i)) >> i
    q = (x & (1 << j)) >> j
    x = _set(x, p, j)
    x = _set(x, q, i)
    return x

print(swapbits(739999999999999, 363, 343434))