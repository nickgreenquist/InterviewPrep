def maxWidthOfVerticalArea(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    x_vals = sorted([point[0] for point in points])
    max_dist = 0
    for i in range(len(x_vals) - 1):
        max_dist = max(max_dist, x_vals[i+1] - x_vals[i])
    return max_dist

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]] # output = 3

print(maxWidthOfVerticalArea(points) == 3)