import heapq

while True:
    heapq
    n = int(input())
    if n  == 0:
        break
    nums = input().split()
    total = 0
    test = []
    for i in range(n):
        test.append(int(nums[i]))
    heapq.heapify(test)
    print(test)

    while len(test) > 0:
        c = heapq.nsmallest(1, test)
        d = heapq.nsmallest(1, test)
        s = (c[0] + d[0])
        total += s
        heapq.heappush(test, s)
    print(total)


    
'''
3
1 2 3
4
1 2 3 4
0
'''