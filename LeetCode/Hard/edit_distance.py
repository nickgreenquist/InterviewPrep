class Solution:
    def minDistance(self, word1, word2):
        dp = []
        for i in range(len(word1) + 1):
            dp.append([])
            for j in range(len(word2) + 1):
                dp[i].append(0)
        
        # base cases - > edit distance null string to word1 and word2
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(len(word2) + 1):
            dp[0][i] = i
        
        # left diagnol, bottom up solution
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                c1 = word1[i-1]
                c2 = word2[j-1]
                
                if c1 == c2:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # min cost of add, delete, replace
                    replace = dp[i-1][j-1]
                    add = dp[i][j-1]
                    delete = dp[i-1][j]
                    dp[i][j] = min(replace, add, delete) + 1
        
        return dp

'''
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
'''

s = Solution()
word1 = "horse"
word2 = "ros"
dp = s.minDistance(word1, word2)
print("min distance", dp[len(word1)][len(word2)])

# get edits using dp
i = len(word1)
j = len(word2)

while i > 0 and j > 0:
    if word1[i-1] == word2[j-1]: # no edit
        i -= 1
        j -= 1
    else:
        replace = dp[i-1][j-1]
        add = dp[i][j-1]
        delete = dp[i-1][j]
        min_move = min(replace, add, delete)

        if min_move == replace:
            print("replace", word1[i-1], "->", word2[j-1])
            i -= 1
            j -= 1
        elif min_move == add:
            print("add", word2[j-1])
            j -= 1
        elif min_move == delete:
            print("delete", word1[i-1])
            i -= 1
    