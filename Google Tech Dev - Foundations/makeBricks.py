'''
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return true if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. 
See also: Introduction to MakeBricks
'''

def makeBricks(small, big, goal):
    # check if enough big bricks and small bricks to cover
    if goal > big*5 + small:
        return False

    # we know we have more than enough, but check if possile to make whole bricks work
    if goal % 5 > small:
        return False
    return True
    

print(makeBricks(3, 1, 8)) # true
print(makeBricks(3, 1, 9)) # false
print(makeBricks(3, 2, 10)) # true