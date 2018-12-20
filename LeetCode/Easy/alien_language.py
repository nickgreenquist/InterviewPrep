'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.
'''

def isAlienSorted(words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """
    position = {}
    for i in range(len(order)):
        position[order[i]] = i
    
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i+1]
        
        # first let's check if w2 is simply a prefix of w1
        m = len(w2)
        if w2 == w1[:m] and len(w1) > len(w2):
            return False
        
        j = 0
        while j < len(w1) and j < len(w2):
            if position[w1[j]] > position[w2[j]]: 
                return False
            elif position[w1[j]] == position[w2[j]]:
                j += 1
            else:
                break
    return True

'''
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
'''
print(isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))

'''
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: 'app' is lexigraphically smaller than 'apple'
'''
print(isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
        