n = int(input())
starts = []
ends = []
for i in range(n):
    inp = input().split()
    start = int(inp[0])
    end = int(inp[1])
    
    starts.append(start)
    ends.append(end)

starts = sorted(starts)
print(starts)
ends = sorted(ends)
print(ends)
tvs_in = 1
max_tvs = 1
time = starts[0]

i = 1
j = 1
while i < n and j < n:
    if starts[i] <= ends[j]:
        tvs_in += 1
        max_tvs = max(max_tvs, tvs_in)
        i += 1
    else:
        tvs_in -= 1
        j += 1
print(max_tvs)
if max_tvs <= 2:
    print("YES")
else:
    print("NO")


