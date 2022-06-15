import random

class Solution:
    def __init__(self, w):
        self.h = []
        s = 0
        for i in w:
            s += i
            self.h.append(s)
        
    def bs(self, A, T):
        L = 0
        R = len(A) - 1
        while L <= R:
            m = L + ((R - L) // 2)
            if A[m] < T:
                L = m + 1
            elif A[m] > T:
                R = m - 1
            else:
                return m
        return -L - 1
        
    def pickIndex(self):
        rand_idx = random.randint(1, self.h[-1])
        r = self.bs(self.h, rand_idx)
        if r < 0:
            return -r - 1
        
        return r

w = [1,5,2,2]

s = Solution(w)
picks = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
}
for i in range(100000):
    pick = s.pickIndex()
    picks[pick] += 1

print(picks)