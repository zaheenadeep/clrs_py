def rprop(x):
    if x == 0:
        return 0
    else:
        return x | (x - 1)

print(bin(rprop(0b10100000)))