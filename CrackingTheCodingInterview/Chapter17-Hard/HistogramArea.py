"""
Imagine a histogram (bar graph).
Design an algorithm to compute the volume of water it could hold
if someone poured water across the top. You can assume that each
histogram bar has width 1
"""
def area_of_histrogram(hist):
    left_max = []
    l_max = float('-inf')
    for height in hist:
        l_max = max(l_max, height)
        left_max.append(l_max)
    
    i = len(hist) - 1
    r_max = float('-inf')
    total = 0
    while i >= 0:
        height = hist[i]
        r_max = max(r_max, height)
        total += min(r_max, left_max[i]) - height
        i -= 1
    return total


hist = [0,0,4,0,0,6,0,0,3,0,8,0,2,0,5,2,0,3,0,0]
area = area_of_histrogram(hist)
print(area)
assert 46 == area