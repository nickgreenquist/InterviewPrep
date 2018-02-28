code = input()
while code != '0':
    n = len(code)
    count = {}
    count[0] = 1
    count[1] = 1

    for i in range(2, n+1):
        count[i] = 0

        if code[i-1] > '0':
            count[i] = count[i-1]

        if code[i-2] == '1' or (code[i-2] == '2' and code[i-1] < '7'):
            count[i] += count[i-2]
    print(count[n])



    code = input()