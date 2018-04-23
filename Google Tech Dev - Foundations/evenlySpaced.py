'''
Given three ints, a b c, one of them is small, one is medium and one is large. 
Return true if the three values are evenly spaced, so the difference between 
small and medium is the same as the difference between medium and large.
'''

def evenlySpaced(a, b, c):
    small = min(a,b,c)
    big = max(a,b,c)
    if a != big and a != small:
        medium = a
    elif b != big and b != small:
        medium = b
    else:
        medium = c
    
    return big - medium == medium - small

print(evenlySpaced(2, 4, 6)) # true
print(evenlySpaced(4, 6, 2)) # true
print(evenlySpaced(4, 6, 3)) # false