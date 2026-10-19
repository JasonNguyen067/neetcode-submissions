# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # For this we want to be able to recursively pass in the child nodes, 
        # But at the same time we want some sort of way to track the current max val
        # Because it says a good node is the path to that node thers no nodes GREATER then x so x >=

        def path(curr, maxVal):
            if not curr:
                return 0

            goodNodes = 0

            if curr.val >= maxVal:
                goodNodes = 1

            maxVal = max(maxVal, curr.val)

            goodNodes += path(curr.left, maxVal)
            goodNodes += path(curr.right, maxVal)

            return goodNodes            

        return path(root, root.val)

        