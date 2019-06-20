'''
You have a set of tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make.
'''

def numTilePossibilities(tiles):
    bag = {}
    letters = set()
    for c in tiles:
        letters.add(c)
        if c in bag:
            bag[c] += 1
        else:
            bag[c] = 1
    letters = list(letters)
    
    # build implicit tree from bag of letters
    def traverse(bag, letters):
        count = 0
        for c in letters:
            if bag[c] > 0:
                count += 1
                
                # take letter out of bag and traverse
                bag[c] -= 1
                count += traverse(bag, letters)
                
                # put letter back in the bag
                bag[c] += 1
        return count
    
    count = traverse(bag, letters)
    return count

'''
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
'''
print(numTilePossibilities('AAB'))

'''
Input: "AAABBC"
Output: 188
'''
print(numTilePossibilities('AAABBC'))