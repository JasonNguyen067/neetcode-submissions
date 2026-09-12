# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxATM):
            if not node:
                return 0

            count = 0

            if node.val >= maxATM:
                count = 1

            maxATM = max(maxATM, node.val)

            count += dfs(node.left, maxATM)
            count += dfs(node.right, maxATM)

            return count

        return dfs(root, root.val)