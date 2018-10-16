'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
'''

def minWindow(s, t):
    count = {}
    for c in t:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    
    i = 0
    j = 0
    head = 0 # start of the best substring
    d = float('inf') # length of best substring
    counter = len(t) # used to check if substring is valid
    
    while j < len(s):
        # reduce the counter when we find a needed target char
        if s[j] in count and count[s[j]] > 0:
            counter -= 1
            
        # reduce the number of this target char needed
        # can be negative signalling we have more than enough to use
        if s[j] in count:
            count[s[j]] -= 1
            
        j += 1
        
        # found valid window, so try and shrink it
        while counter == 0:
            # found better min substring, so update head of it and its length
            if j - i < d:
                d = j - i
                head = i
            
            # we've used this char, so signal we used one up
            if s[i] in count:
                count[s[i]] += 1
            
            # if the char is in target and count needed for this char is
            # back above 0, we have to break the loop and signal we need to find
            # a new one of this target character
            if s[i] in count and count[s[i]] > 0:
                counter += 1
            
            i += 1
    
    if d != float('inf'):
        return s[head:head + d]
    return ""
            
'''
Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
'''       
print(minWindow(s = "ADOBECODEBANC", t = "ABC")) 
     