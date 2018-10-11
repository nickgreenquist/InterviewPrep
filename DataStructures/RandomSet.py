from random import randint

class RandomizedSet(object):

    def __init__(self):
        self.set = []
        self.pos = {} # maps value back to position in set
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        n = len(self.set)
        self.set.append(val)
        self.pos[val] = n
        
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        
        # if val is last element in set, just pop and clear the key
        if self.set[-1] == val:
            self.set.pop()
            self.pos.pop(val, None)
        else:
            # find the index of where val is and pop val from pos
            index = self.pos[val]
            self.pos.pop(val, None)
            
            # overwrite the index where val was with the last val in the set and update pos
            last_val = self.set.pop()
            self.set[index] = last_val
            self.pos[last_val] = index
        
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        index = randint(0, len(self.set) - 1)
        return self.set[index]
        

# Test this RandomSet Data Structure
rs = RandomizedSet()
for i in range(10): 
    rs.insert(i)

rs.remove(5)
rs.remove(7)

dist = {}
for i in range(10000):
    randval = rs.getRandom()
    if randval in dist:
        dist[randval] += 1
    else:
        dist[randval] = 1

for k,v in dist.items():
    print("{}: {}".format(k, v))