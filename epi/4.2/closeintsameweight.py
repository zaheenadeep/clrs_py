def closeintsameweight(x):
    if x & 1 == 1:
        last0as1 = x ^ (x+1)
        last0as1 += 1
        last0as1 >>= 1
        return (x | last0as1) ^ (last0as1 >> 1)
    else:
        last1 = x ^ (x-1)
        last1 += 1
        last1 >>= 1
        return (x ^ last1) | (last1 >> 1)

print(bin(closeintsameweight(0b11111)))