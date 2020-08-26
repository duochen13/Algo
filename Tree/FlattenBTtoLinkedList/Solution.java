

//    1
//   / \
//  2   5
// / \   \
// 3   4   6

// 1
//  \
//   2
//    \
//     3
//      \
//       4
//        \
//         5
//          \
//           6

// Before starting
// Of course its binary tree, not binary search tree


// General idea


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

//        1(cur)
//     /       \
//  2(cur.l)    5(cur.r)
//   \            \
//    \            \
//   tmp = cur.r
//   cur.r = cur.l
//   cur.l's leaf right node = tmp

class Solution {
    public void flatten(TreeNode root) {
        if (root == null) return;

        TreeNode preLeft = root.left;
        TreeNode preRight = root.right;
        root.left = null;

        // error: flattern(root.right), cuz on line65, assign preLeft instead of root.left
        flatten(preRight);
        flatten(preLeft);

        root.right = preLeft;
        TreeNode cur = root;
        while (cur.right != null) {
            cur = cur.right;
        }
        cur.right = preRight;
    }
}
