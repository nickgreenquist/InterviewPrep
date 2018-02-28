from collections import Counter

def print_sorted_with_count(accounts):
    counts = Counter(accounts)
    for account, count in sorted(counts.items()):
        print('{} {}'.format(account, count))

t = int(input())
for i in range(t):
    accounts = []
    n = int(input())
    for j in range(n):
        a = input().strip()
        accounts.append(a)
    if i < t - 1:
        input()
    print_sorted_with_count(accounts)
    print()