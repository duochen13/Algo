"""
Given an array of n points in the plane, and the problem is to find out the closest pair of points in the array. This problem arises in a number of applications. For example, in air-traffic control, you may want to monitor planes that come too close together, since this may indicate a possible collision. Recall the following formula for distance between two points p and q.
"""



def ClosestPoints(points):
    res = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            res = min(res, d)
    return res


"""
1. sort(key=lambda x : x[1])
2. split points[:mid] and points[mid + 1:]
3. d = min(dl, dr)
4. construct strip list [mid-d, mid + d]
"""


# A utility function to find the distance between the closest points of 
# strip of a given size. All points in strip[] are sorted according to 
# y coordinate. They all have an upper bound on minimum distance as d. 
# Note that this method seems to be a O(n^2) method, but it's a O(n) 
# method as the inner loop runs at most 6 times 
def stripCloest(strip, j, d):
    res = d
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            x1, y1 = strip[i]
            x2, y2 = strip[j]
            d = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if d < res:
                res = d
    return res


# min length within list of points
# T(n) = 2*T(n/2) + O(n)
def helper(points, n):
    if n <= 3:
        return ClosestPoints(points)
    mid = n // 2
    dl = helper(points, mid)
    dr = helper(points, n - mid)
    d = min(dl, dr)
    # find strip list
    curx, _ = points[mid]
    strip = []
    j = 0
    for i in range(n):
        x, y = points[i]
        if abs(x - curx) <= d:
            strip.append([x, y])
            j += 1
    return stripCloest(strip, j, d)


def StripClosestPoints(points):
    return helper(points, len(points))




if __name__ == '__main__':
    points = [[2,3],[12,30],[40,50],[5,1],[12,10],[3,4]]
    res = ClosestPoints(points)
    res_ = StripClosestPoints(points)
    assert res == res_
    print(res_)