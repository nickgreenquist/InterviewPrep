def isValid(s: str) -> bool:
    closers_to_opens = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    opens = set(['(', '{', '['])
    
    # shared stack, so 'closing' has to match last open
    stack = []
    
    for c in s:
        # if new 'open'
        if c in opens:
            stack.append(c)

        # if a close, we need to check last 'open'
        elif c in closers_to_opens:
            # no opens, so invalid
            if len(stack) < 1:
                return False

            openc = stack.pop()

            # if the last 'open' does not match this 'close
            if openc != closers_to_opens[c]:
                return False
                
    # leftover 'open's means invalid
    if len(stack) > 0:
        return False
            
    return True

