def modpowtwo(x, pow):
    return x & (pow - 1)

print(modpowtwo(77, 32))