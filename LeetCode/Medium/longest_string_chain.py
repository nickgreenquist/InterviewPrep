'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.
For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.
'''

def longestStrChain(words):
    words = sorted(words, key=len)
    
    best = {}
    for word in words:
        best[word] = 1
    
    # go through each word, strip each possible char, and check if the stripped word is in the bag of words
    # update best chain lenght ending eith each word by using the stripped word's best chain value
    for word in words:
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in best:
                best[word] = max(best[word], best[prev] + 1)
    
    longest_chain = 0
    for k,v in best.items():
        longest_chain = max(longest_chain, v)
    return longest_chain

'''
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
'''
print(longestStrChain(["a","b","ba","bca","bda","bdca"]))