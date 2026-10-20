# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Need a way to track the height as the calls go back up
        # We can go with dfs for this one, and compare with left and right via the depth

        def dfs(curr):
            if not curr:
                return True

            left = dfs(curr.left)
            right = dfs(curr.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        # we discard so we dont care abt height value we just care whether its -1 or not 
        # Return if its -1 false if not true

        return dfs(root) != -1