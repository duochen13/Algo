#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# recursion
def isValidBST_recursion(TreeNode):
	def dfs(node, lower, upper):
		if not node:
            return True
        if node.val >= upper or node.val <= lower:
			return False
	    return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
	return dfs(root, float('-inf'), float('inf'))


# iteration
def isValidBST_iteration(TreeNode):
    if not root:
        return True
    stack = [(root, float('-inf'), float('inf'))]
    while stack:
        cur_node, lower, upper = stack.pop()
        if cur_node.val <= lower or cur_node.val >= upper:
            return False
        if cur_node.left:
            stack.append((cur_node.left, lower, cur_node.val))
        if cur_node.right:
            stack.append((cur_node.right, cur_node.val, upper))
    return True
