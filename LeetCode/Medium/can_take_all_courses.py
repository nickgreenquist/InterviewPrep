
def canFinish(numCourses, prerequisites):S
    adj_list = {}
    for p in prerequisites:
        source = p[1]
        dest = p[0]
        if source in adj_list:
            adj_list[source].append(dest)
        else:
            adj_list[source] = [dest]
            
    inblocks = {}
    for k,v in adj_list.items():
        for dest in v:
            if dest in inblocks:
                inblocks[dest] += 1
            else:
                inblocks[dest] = 1
    
    q = []
    for i in range(numCourses):
        if i not in inblocks:
            q.append(i)
    
    count = 0
    while len(q) > 0:
        course = q.pop(0)
        count += 1
        if course in adj_list:
            for dest in adj_list[course]:
                inblocks[dest] -= 1
                if inblocks[dest] == 0:
                    q.append(dest)
    
    return count == numCourses