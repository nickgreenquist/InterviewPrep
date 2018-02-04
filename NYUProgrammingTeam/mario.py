t = int(input())
for i in range(0, t):
    n = int(input())
    walls = input()
    walls = walls.split()
    for k in range(0, n):
        walls[k] = int(walls[k])
    
    lastnum = 1000000000000000000
    high = 0
    low = -1
    for k in range(0, n):
        if walls[k] > lastnum:
            high += 1
        if walls[k] < lastnum:
            low += 1
        
        lastnum = walls[k]
    
    print("Case " + str(i + 1) + ": " + str(high) + " " + str(low))