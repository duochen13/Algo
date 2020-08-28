/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    // 235
    public TreeNode lowestCommonAncestorBT(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode node = root;
        
        while (node != null) {
            // left side
            if (Math.max(p.val, q.val) < node.val) {
                node = node.left;
            } // right side
            else if (Math.min(p.val, q.val) > node.val) {
                node = node.right;
            } else {
                return node;
            }
        }
        
        return node;
    }

    //236
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == p || root == q || root == null) {
            return root;
        }
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        return (left != null && right != null) ? root : (left != null ? left : right);
    }
}