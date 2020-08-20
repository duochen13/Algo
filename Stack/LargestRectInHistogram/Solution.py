
def largestRectangleArea(heights):
    """
    type: a list of integers
    """
    stack = [] # stores the left boundary
    res = 0
    i = 0
    while i < len(heights):
        h = heights[i]
        if not stack or h > heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            tmp_index = stack.pop()
            area = heights[tmp_index] * (i - tmp_index + 1)
            res = max(res, area)
    while stack:
        tmp = stack.pop()
        area = heights[tmp] * ((i - stack[-1] - 1) if stack else i)
    return res if not stack else heights[stack[0]]



heights = [2,1,5,6,2,3]
res = largestRectangleArea(heights)
print(res)

# 0 1 2 3 4 5
# 6 2 5 4 5 1 6
#       ^
# stack: [1]
# tmp: 5 * (3 - 1 - 1) = 
# area: 
# res: 6