/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int maxD;

    public int diameterOfBinaryTree(TreeNode root) {
        height(root);
        return maxD;
    }

    public int height(TreeNode root){
        if (root == null){
            return 0;
        }
        int lh = height(root.left);
        int rh = height(root.right);
        int dthrunode = lh + rh;

        maxD = Math.max(maxD, dthrunode);

        return 1 + Math.max(lh,rh);


    }
}
