
def traverse(left, right, output, current):
    if right > left:
        return
    if right < 1 and left < 1:
        output.append(current)
        return
    if left:
        traverse(left - 1, right, output, "(" + current)
    if right:
        traverse(left, right - 1, output, ")" + current)

def generateParenthesis(n):
    if n < 1:
        return []
    output = []
    traverse(n, n, output, "")
    return output

'''
input: 3
output: 
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
for row in generateParenthesis(3):
    print(row)