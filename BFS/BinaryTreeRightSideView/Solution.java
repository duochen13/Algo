
// Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

// Input: [1,2,3,null,5,null,4...]
// Output: [1, 3, 4, 6]
// Explanation:

//    1            <---
//  /   \
// 2     3         <---
//  \     \
//   5     4       <---
//  /
// 6 

// bfs with queue
// [1]                  1
// [2, 3]               3
// [3, 5]  -> [5, 4]    4
// [4, 6]  -> [6]       6
// []

import java.util.List;
import java.util.Queue;
import java.util.Deque;
import java.util.LinkedList;

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

    public 

    // level order BFS
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) {
            return new ArrayList<Integer>();
        }
        Deque<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        List<Integer> res = new ArrayList<Integer>();

        while (!queue.isEmpty()) {
            int N = queue.size();
            for (int i = 0; i < N; ++i) {
                TreeNode cur = queue.poll();

                if (i == N - 1){
                    res.add(cur.val);
                }

                if (cur.left != null) {
                    queue.add(cur.left);
                } if (cur.right != null) {
                    queue.add(cur.right);
                }
            }
        }

        return res;
    }
}