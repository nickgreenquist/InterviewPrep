def countConsistentStrings(allowed, words):
    """
    :type allowed: str
    :type words: List[str]
    :rtype: int
    """
    allowed_set = set(allowed)
    num_consistent = 0
    for word in words:
        is_consistent = True
        for c in word:
            if c not in allowed_set:
                is_consistent = False
                break
        if is_consistent:
            num_consistent += 1
    return num_consistent

'''
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
'''

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
expected = 4

print(countConsistentStrings(allowed, words) == 4)