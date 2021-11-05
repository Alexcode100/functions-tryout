def multiplier(n):
    return lambda a : a * n

mytripler = multiplier(3)

print(mytripler(11))