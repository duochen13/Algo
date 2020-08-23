// Given a binary tree, determine if it is height-balanced.
// For this problem, a height-balanced binary tree is defined as:
// a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {

    // bottom up O(n) solution, if use top-dowm(return 1 + height(...)), double count depth in isBalanced(...), time complexity is O(n^2)
    public int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftHeight = dfs(node.left);
        if (leftHeight == -1) return -1;
        int rightHeight = dfs(node.right);
        if (rightHeight == -1) return -1;
        if (Math.abs(leftHeight - rightHeight) > 1) {
            return -1;
        }
        return Math.max(leftHeight, rightHeight) + 1;
    }

   
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        return dfs(root) != -1;
    }
   

    // top down method
    public int heightTopDown(TreeNode node, int curHeight) {
        if (node == null) {
            return curHeight;
        }
        int leftHeight = height(node.left, curHeight + 1);
        int rightHeight = height(node.right, curHeight + 1);
        return Math.max(leftHeight, rightHeight);
    }

    public boolean isBalancedTopDown(TreeNode root) {
        if (root == null) return true;
        return Math.abs(height(root.left, 0) - height(root.right, 0)) <= 1 && isBalanced(root.left) && isBalanced(root.right);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        TreeNode leftNode = root.left;
        leftNode.right = new TreeNode(4);
        System.out.println(s.isBalanced(root));
    }
}