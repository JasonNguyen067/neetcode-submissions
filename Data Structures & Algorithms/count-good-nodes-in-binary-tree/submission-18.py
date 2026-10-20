# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(curr, maxVal):
            if not curr:
                return 0

            goodNode = 0

            if curr.val >= maxVal:
                goodNode = 1

            maxVal = max(maxVal, curr.val)

            goodNode += dfs(curr.left, maxVal)
            goodNode += dfs(curr.right, maxVal)

            return goodNode

        return dfs(root, root.val)