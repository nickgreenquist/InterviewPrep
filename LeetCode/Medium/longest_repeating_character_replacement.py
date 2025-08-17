def findMaxChar(char_to_count):
    maxCount = 0
    maxChar = ''
    for k,v in char_to_count.items():
        if v > maxCount:
            maxCount = v
            maxChar = k
    return maxChar

def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    left = 0
    right = 0
    char_to_count = {}

    max_seen = 0
    while right < len(s):
        if s[right] in char_to_count:
            char_to_count[s[right]] += 1
        else:
            char_to_count[s[right]] = 1

        # check if current window is valid
        max_char = findMaxChar(char_to_count)
        max_char_count = char_to_count[max_char]
        window_length = right - left + 1
        if window_length - max_char_count <= k: # valid
            max_seen = max(max_seen, window_length)
        else:
            char_to_count[s[left]] -= 1
            left += 1
        
        right += 1

    return max_seen

print(characterReplacement(s = "ABAB", k = 2))