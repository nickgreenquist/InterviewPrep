class WordDictionary(object):

    def __init__(self):
        self.tri = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        tri = self.tri
        for c in word:
            if c not in tri:
                tri[c] = {}
            tri = tri[c]
        tri['#'] = '#' # end of word
        

    def search_internal(self, word, i, tri):
        if i > len(word):
            return False
        if tri == '#': # went too far in our tri
            return False
        if i == len(word):
            return '#' in tri
            
        c = word[i]
        if c in tri:
            return self.search_internal(word, i + 1, tri[c])
        if c == '.':
            for k,v in tri.items():
                found = self.search_internal(word, i + 1, v)
                if found:
                    return True
        return False

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.search_internal(word, 0, self.tri)
            

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("bag")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.tri)
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True