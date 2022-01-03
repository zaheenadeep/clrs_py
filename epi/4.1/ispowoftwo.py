def ispowoftwo(x):
    if x == 0:
        return False
    else:
        return not (x & (x - 1))

print(ispowoftwo(0))