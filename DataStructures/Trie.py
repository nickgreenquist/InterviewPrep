class Node(object):
    def __init__(self, c):
        self.c = c
        self.children = []
        self.isWord = False

class Trie(object):
    def __init__(self):
        self.root = Node("")

    def _insert(self, word, i, root):
        if i >= len(word):
            root.isWord = True
            return

        # check if any children have this letter
        for child in root.children:
            if child.c == word[i]:
                self._insert(word, i+1, child)
                return
        
        # no child has this letter, make a new Node
        child = Node(word[i])
        root.children.append(child)
        self._insert(word, i+1, child)
        
    def insert(self, word):
        self._insert(word, 0, self.root)

    def _search(self, word, i, root):
        # if we made it to the last letter in word, check if the root is valid word
        if i >= len(word):
            return root.isWord

        # check if any children's characters match word[i]
        for child in root.children:
            if child.c == word[i]:
                return self._search(word, i+1, child)
        
        # no further children and more of the word to search for means no match
        return False

    def search(self, word):
        return self._search(word, 0, self.root)

t = Trie()
t.insert("doruk")
t.insert("foruk")
t.insert("dom")
t.insert("bobst")
t.insert("frank")
t.insert("for")

print("is {} in the trie: {}".format('doruk', t.search('doruk')))
print("is {} in the trie: {}".format('foruk', t.search('foruk')))
print("is {} in the trie: {}".format('bobst', t.search('bobst')))
print("is {} in the trie: {}".format('nick', t.search('nick')))
print("is {} in the trie: {}".format('for', t.search('for')))
