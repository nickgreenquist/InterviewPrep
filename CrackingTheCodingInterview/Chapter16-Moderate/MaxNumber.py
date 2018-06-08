def flip(bit):
    return 1^bit

def sign(a):
    return flip((a >> 31) & 0x1)

def get_max(a, b):
    k = sign(a-b)
    q = flip(k)
    return (a * k) + (b * q)

print(get_max(10, 88))