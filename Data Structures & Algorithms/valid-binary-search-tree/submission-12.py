# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validity(lower, node, upper):
            if not node:
                return True

            if not (lower < node.val < upper):
                return False

            left = validity(lower, node.left, node.val)
            right = validity(node.val, node.right, upper)

            return left and right

        return validity(float("-inf"), root, float("inf"))