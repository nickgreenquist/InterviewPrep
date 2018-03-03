

def main():
    n = int(input())
    while n != 0:
        seen = set()
        count = 0
        max_count = 0
        for i in range(n):
            c = input()
            if c not in seen:
                count+=1
                seen.add(c)
            else:
                max_count = max(count, max_count)
                count = 1
                seen.clear()
                seen.add(c)
        print(max_count)
        max_count = 0
        count = 0
        n = int(input())

if __name__ == "__main__":
    main()

'''
7
1
5
1
2
3
2
1
0
'''