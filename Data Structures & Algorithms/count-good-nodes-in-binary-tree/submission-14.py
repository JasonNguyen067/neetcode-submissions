# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Lets create a function
        # Inside this function we want to track the current node and the maxVAL
        # If the case where the current node isnt greater than maxVal then we dont return a +1 count

        def dfs(curr, MAXVAL):
            if not curr:
                return 0

            count = 0

            if curr.val >= MAXVAL:
                count = 1

            MAXVAL = max(MAXVAL, curr.val)

            count += dfs(curr.left, MAXVAL)
            count += dfs(curr.right, MAXVAL)

            return count

        return dfs(root, root.val)