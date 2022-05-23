def longestValidParentheses(s: str) -> int:
    n = len(s)
    opens = []
    longest = [0 for i in range(n)]
    
    for i in range(n):
        c = s[i]
        if c == '(':
            opens.append(i)
        elif c == ')':
            if len(opens) >= 1:
                k = opens.pop()
                longest[i] = i - k
                longest[k] = i - k
    
    # find longest chain of non-zero maxes, max is length of this chain
    longest_chain = 0
    chain = 0
    for i in range(0, n):
        if longest[i] > 0:
            chain += 1
            longest_chain = max(longest_chain, chain)
        else:
            chain = 0
    return longest_chain

test_strings = [
    "(()",
    ")()())"
]
for s in test_strings:
    print(s + ': ' + str(longestValidParentheses(s)))
    print()