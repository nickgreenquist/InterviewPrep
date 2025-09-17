def numberOfOnesSet(x):
    count = 0
    while x:
        print(bin(x))
        print(bin(x-1))
        print(bin(x & (x-1)))
        print()

        x = x & (x-1)
        count += 1
    return count

# mod by 2, shift all bits to right, mod by 2, etc.
def numberOfOnesSetWithMod(x):
    count = 0
    while x:
        if x % 2 == 1:
            count += 1

        x = x >> 1
    return count

print('Using x & (x-1)')
print(numberOfOnesSet(11))
print()
print(numberOfOnesSet(128))
print()

print('Using x % 2 and >>')
print(numberOfOnesSetWithMod(11))
print()
print(numberOfOnesSetWithMod(128))
print()

