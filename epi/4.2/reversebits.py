rev = dict()

def rev16bits(x):
	val = x
	for i in range(8):
		j = 16 - i - 1
		ibit = (x >> i) & 1
		jbit = (x >> j) & 1
		if ibit != jbit:
			val = x ^ ((1 << i) | (1 << j))
	rev[x] = val

for num in range(0x10000):
	rev16bits(num)


def reversebits(x):
	MASK = 0xFFFF
	NMASK = 16

	rval =  rev[ x >> (3 * NMASK) ]
	rval |= rev[(x >> (2 * NMASK)) & MASK]   << NMASK
	rval |= rev[(x >> NMASK) & MASK]         << (2 * NMASK)
	rval |= rev[ x & MASK ]                  << (3 * NMASK)

	return rval

print(bin(reversebits(0b100011100)))