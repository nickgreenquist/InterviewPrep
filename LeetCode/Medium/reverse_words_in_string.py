class WordReverser(object):
    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    
    def reverseWord(self, s):
        i = 0
        j = 0
        while i < len(s):
            while j < len(s) and s[j] != ' ':
                j += 1
            self.reverse(s, i, j-1)
            
            # find next non space
            i = j
            while i < len(s) and s[i] == ' ':
                i += 1
                
            # compact space in between words
            for k in range(i-j-1):
                s.pop(j)
            
            i = j+1
            j = i     
            
    def stripWhitespace(self, s):
        i = 0
        while i < len(s) and s[i] == ' ':
            s.pop(0)
        
        j = len(s) - 1
        while j >= 0 and s[j] == ' ':
            s.pop(j)
            j -= 1

    def reverseWords(self, s):
        s = [c for c in s]
        
        # 1. reverse entire 
        self.reverse(s, 0, len(s) - 1)
        
        # 2. reverse individual words
        self.reverseWord(s)
        
        # 3. strip trailing and leading whitespace 
        self.stripWhitespace(s)
        
        s = "".join(s)
        return s

s = "  the sky       is  blue "
print(s)
reverser = WordReverser()
s = reverser.reverseWords(s)
print(s)