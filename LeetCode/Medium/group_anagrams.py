def groupAnagrams(strs):
    groups = {}
    for word in strs:
        # get a sorted tuple of all the characters in each word
        char_set = tuple(sorted(word))
        
        # check if that char_set is a group
        if char_set in groups:
            groups[char_set].append(word)
        else:
            groups[char_set] = [word]
    
    # the values of each char_set is a list of words with that char_set
    return groups.values()

'''
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(words))