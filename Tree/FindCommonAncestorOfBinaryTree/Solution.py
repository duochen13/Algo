
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        node = root
        while node:
            if max(p, q) < node.val:
                node = node.left
            elif min(p, q) > node.val:
                node = node.right
            else:
                return node