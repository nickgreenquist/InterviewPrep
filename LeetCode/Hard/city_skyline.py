import heapq
class MaxQueue(object):
    def __init__(self):
        self.q = []
    def push(self, val):
        heapq.heappush(self.q,-val)
    def pop(self):
        return -heapq.heappop(self.q)
    def peek(self):
        return -self.q[0]
    def remove(self, val):
        self.q.remove(-val)
        heapq.heapify(self.q)
    
class Solution(object):
    def parseBuildings(self, buildings):
        points = [] # (x, height, 's'/'e')
        for b in buildings:
            points.append((b[0], b[2], 's'))
            points.append((b[1], b[2], 'e'))
        return sorted(points)
    
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # merge any same heigh and touching buildings
        i = 0
        buildings_merged = []
        while i < len(buildings):
            j = i + 1
            while j < len(buildings) and buildings[i][1] == buildings[j][0] and buildings[i][2] == buildings[j][2]:
                buildings[i][1] = buildings[j][1]
                j += 1
                
            buildings_merged.append(buildings[i])
            i = j
                
        points = self.parseBuildings(buildings_merged)
        
        mq = MaxQueue()
        mq.push(0)
        
        skyline = []
        for p in points:
            old_max = mq.peek()
            if p[2] == 's':
                mq.push(p[1])
                if old_max != mq.peek():
                    skyline.append([p[0], p[1]])
            else:
                mq.remove(p[1])
                if old_max != mq.peek():
                    skyline.append([p[0], mq.peek()])
         
        # merge any touching points, take taller height
        i = 0
        skyline_merged = []
        while i < len(skyline):
            j = i + 1
            while j < len(skyline):
                if skyline[j][0] == skyline[i][0]:
                    skyline[i][1] = max(skyline[i][1], skyline[j][1])
                    j += 1
                else:
                    break
            skyline_merged.append(skyline[i])
            i = j
            
        return skyline_merged
            