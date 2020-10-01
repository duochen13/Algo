# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isLeafNode(self, node):
        return not node.left and not node.right
    
    def findLeftNodes(self, node, res):
        if not node:
            return
        # avoid double count with leaf nodes
        if not self.isLeafNode(node):
            res.append(node.val)
        if node.left:
            self.findLeftNodes(node.left, res)
        else:
            self.findLeftNodes(node.right, res)
        
        
    def findRightNodes(self, node, res):
        if not node:
            return
        if node.right:
            self.findRightNodes(node.right, res)
        else:
            self.findRightNodes(node.left, res)
        # counterclockwise order and avoid double count with leaf nodes
        if not self.isLeafNode(node):
            res.append(node.val)
        
        
    def findLeafNodes(self, node, res):
        if not node:
            return
        # the current node is leaf node
        if not node.left and not node.right:
            res.append(node.val)
            return
        self.findLeafNodes(node.left, res)
        self.findLeafNodes(node.right, res)
        
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # error handling
        if not root:
            return []
        res = []
        # avoid double count in leafnode and left/right nodes
        if root.left or root.right:
            res.append(root.val)
        
        self.findLeftNodes(root.left, res)
        print("res:{}".format(res))
       
        self.findLeafNodes(root, res)
        print("res:{}".format(res))
    
        self.findRightNodes(root.right , res)
        print("res:{}".format(res))
        
        
        return res
        