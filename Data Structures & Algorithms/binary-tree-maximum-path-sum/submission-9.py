# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        best = float("-inf") # for the case where only onenode is negative, but -3 can't override 0

        def dfs(curr):
            if not curr:
                return 0

            nonlocal best

            left = max(dfs(curr.left), 0) #but we want good paths and negative is possible so take 0 if its less than that
            right = max(dfs(curr.right), 0)

            best = max(best, right + left + curr.val)

            return curr.val + max(left, right)

        dfs(root)

        return best