def longestSubstring(s, k):
    if len(s) < k:
        return 0
    
    # find the character with the smallest count
    min_char_count = float('inf')
    min_char = s[0]
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    for c,v in count.items():
        if v < min_char_count:
            min_char_count = v
            min_char = c
    
    # if this substring's lowest appearing char's count is k or more
    # then this entire substring is a valid substring
    if min_char_count >= k:
        return len(s)
    
    # recursive call on each chunk of this substring split on where the 
    # least occuring character was
    split_by_lowest_char = s.split(min_char)
    best = float('-inf')
    for split in split_by_lowest_char:
        new_s = "".join(split)
        best = max(best, longestSubstring(new_s, k))
    return best
'''
Example 1:
Input:
s = "aaabb", k = 3
Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
'''
print(longestSubstring(s = "aaabb", k = 3))


'''
Example 2:
Input:
s = "ababbc", k = 2
Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times 
'''
print(longestSubstring(s = "ababbc", k = 2))