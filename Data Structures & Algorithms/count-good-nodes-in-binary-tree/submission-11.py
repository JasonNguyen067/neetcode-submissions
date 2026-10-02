# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # The val at whatever node is considered good if nothing is larger than it so node.val >= maxval
        # return count (good nodes)

        if not root:
            return 0

        def dfs(node, MAXVAL):
            if not node:
                return 0

            count = 0

            if node.val >= MAXVAL:
                count = 1
            
            MAXVAL = max(MAXVAL, node.val)

            count += dfs(node.left, MAXVAL)
            count += dfs(node.right, MAXVAL)

            return count

        return dfs(root, root.val)