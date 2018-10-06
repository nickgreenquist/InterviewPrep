class FlipPhone(object):
    def __init__(self):
        mapper = {}
        mapper[1] = []
        mapper[2] = ['a', 'b', 'c']
        mapper[3] = ['d', 'e', 'f']
        mapper[4] = ['g', 'h', 'i']
        mapper[5] = ['j', 'k', 'l']
        mapper[6] = ['m', 'n', 'o']
        mapper[7] = ['p', 'q', 'r', 's']
        mapper[8] = ['t', 'u', 'v']
        mapper[9] = ['w', 'x', 'y', 'z']   
        self.mapper = mapper
        
    def buildCombo(self, digits, i, prefix, combos):
        if i >= len(digits):
            combos.append(prefix)
            return
        
        digit = int(digits[i])
        for letter in self.mapper[digit]:
            self.buildCombo(digits, i + 1, prefix + letter, combos)
    
    def dialOptions(self, digits):
        if len(digits) < 1:
            return []
        combos = []
        self.buildCombo(digits, 0, "", combos)
        return combos

phone = FlipPhone()
print(phone.dialOptions("234"))