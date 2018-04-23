'''
Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. 
Return 0 if they both go over.
'''

def blackjack(a, b):
    if a > 21 and b > 21:
        return 0
    if a > 21:
        return b
    if b > 21:
        return a
        
    dist_a = 21 - a
    dist_b = 21 - b
    if dist_a < dist_b:
        return a
    return b

print(blackjack(19, 21)) # 21
print(blackjack(21, 19)) # 21
print(blackjack(19, 22)) # 19
