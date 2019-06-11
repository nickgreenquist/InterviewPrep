from typing import List

def findOcurrences(text: str, first: str, second: str) -> List[str]:
    tokenized = text.split()
    
    third = []
    i = 0
    while i < len(tokenized) - 2:
        if tokenized[i] == first and tokenized[i+1] == second:
            third.append(tokenized[i+2])
        i += 1
    return third

'''
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
'''
result = findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good")
print(result)