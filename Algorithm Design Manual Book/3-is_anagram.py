def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_counts = {}
    t_counts = {}
    for c in s:
        if c not in s_counts:
            s_counts[c] = 0
        s_counts[c] += 1
    for c in t:
        if c not in t_counts:
            t_counts[c] = 0
        t_counts[c] += 1
    
    for c in s_counts.keys():
        if c not in t_counts:
            return False
        if s_counts[c] != t_counts[c]:
            return False
    
    return True

print(isAnagram('silent', 'listen'))