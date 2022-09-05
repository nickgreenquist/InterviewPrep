class Solution:
    def cut(self, n, memo):
        if n == 1:
            return 1
        if n in memo:
            return memo[n]

        # enumarate all possible break with integer n
        best_product = 0
        for keep in range(n, 1, -1):
            split = n - keep
            if split not in memo:
                memo[split] = self.cut(split, memo)

            product_if_split = keep * memo[split]
            product_if_stay = keep * split
            product_to_use = max(product_if_split, product_if_stay)
            if product_to_use > best_product:
                best_product = product_to_use

        memo[n] = best_product
        return memo[n]

    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        memo = {}
        memo[0] = 0
        memo[1] = 1
        
        self.cut(n, memo)
        
        return memo[n]

s = Solution()
print(s.integerBreak(10))