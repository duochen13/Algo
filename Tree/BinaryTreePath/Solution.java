// Given a binary tree, return all root-to-leaf paths.
// Note: A leaf is a node with no children.

// Input:

//    1
//  /   \
// 2     3
//  \
//   5

// Output: ["1->2->5", "1->3"]

import java.util.Set;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.List;

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

    // recursion
    public void dfs(TreeNode node, String cur, Set<String> res) {
        // null node
        if (node == null) {
            res.add(cur);
            return;
        // leaf node
        } else if (node.left == null && node.right == null) {
            res.add(cur + Integer.toString(node.val));
            return;
        } if (node.right != null) {
            dfs(node.right, cur +  Integer.toString(node.val) + "->", res);
        } if (node.left != null) {
            dfs(node.left, cur + Integer.toString(node.val) + "->", res);
        }
        return;
    }

    public List<String> binaryTreePathsRecursion(TreeNode root) {
        Set<String> res = new HashSet<String>();
        if (root == null) 
            return new ArrayList<String>();

        dfs(root, "", res);

        return new ArrayList<String>(res);
    }

    //    1
    //  /   \
    // 2     3
    //  \
    //   5

    // [(1, "")]
    // [(2, "1->"), (3, "1->")]
    // [(2, "1->")]     add (1->3) to res
    // [(5, "1->2->5")] 
    // []               add (1->2>5) to res

    // iteration
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<String>();
        if (root == null) 
            return new ArrayList<String>();

        Stack<Pair> stack = new Stack<Pair>();
        stack.push(new Pair<TreeNode, String>(root, ""));
        
        while (!stack.isEmpty()) {
            Pair<TreeNode, String> cur = stack.pop();
            TreeNode curNode = cur.getKey();
            String curPath = cur.getValue();
            // leaf node
            if (curNode.left != null && curNode.right != null) {
                res.add(curPath + Integer.toString(curNode.val));
            } 
            if (curNode.left != null) {
                stack.push(new Pair<TreeNode, String>(curNode.left, cur + Integer.toString(curNode.val) + "->"));
            } if (curNode.right != null) {
                stack.push(new Pair<TreeNode, String>(curNode.right, cur + Integer.toString(curNode.val) + "->"));
            }
        }//while

        return res;
    }

}