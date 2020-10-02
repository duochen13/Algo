
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class OSolution:
    # 235
    def lowestCommonAncestorBS(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        node = root
        while node:
            if max(p.val, q.val) < node.val:
                node = node.left
            elif min(p.val, q.val) > node.val:
                node = node.right
            else:
                return node

    # 236
    # 1. LCA exists on both sides
    # 2. LCA exists on node side
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left)
        right = self.lowestCommonAncestor(root.right)
        return root if left and right else left or right
        

class Node:
    def __init__(self, x):
        self.val = x
        self.neighboors = []
    def printTree(self, level):
        # print(self.val, end=" ")
        print("level:{}, val:{}\n".format(level, self.val), end="")
        # print(self.val)
        for node in self.neighboors:
            node.printTree(level + 1)
        


class Solution:
    # N-ary Tree
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        tmp = returnNode = None
        cnt = 0
        for node in root.neighboors:
            tmp = self.lowestCommonAncestor(node, p, q)
            if tmp:
                returnNode = tmp
                cnt += 1
        # print("root.val:{}, cnt:{}".format(root.val, cnt))
        if cnt == 2:
            return root
        elif cnt == 1:
            return returnNode
        return None


if __name__ == '__main__':
    s = Solution()
    node = Node(3)
    node.neighboors = [Node(5), Node(4), Node(1)]
    node_1, node_2, node_3 = [n for n in node.neighboors]
    node_1.neighboors = [Node(6)]
    node_2.neighboors = [Node(7), Node(10), Node(12)]
    p = node_2.neighboors[0]
    node_3.neighboors = [Node(8), Node(9)]
    node_23 = node_2.neighboors[2]
    node_23.neighboors = [Node(13)]
    q = node_23.neighboors[0]

    # node.printTree(level=0)

    res = s.lowestCommonAncestor(root=node, p=p, q=q)

    print(res.val)