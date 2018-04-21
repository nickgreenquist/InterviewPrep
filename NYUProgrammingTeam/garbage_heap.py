test_cases = int(input())
for i in range(test_cases):
    inp = input().split()
    A = int(inp[0])
    B = int(inp[1])
    C = int(inp[2])

    heap = [[0]*B]*A
    for i in range(A):
        for j in range(B):
            heap[i][j] = [0 for i in range(C)]

    inp = input().split()
    l = 0
    for i in range(A):
        for j in range(B):
            for k in range(C):
                heap[i][j][k] = inp[l]
                l += 1
    print(heap[0][0][0])


