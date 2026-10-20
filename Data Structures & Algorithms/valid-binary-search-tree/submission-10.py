# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checker(lower, curr, upper):
            if not curr:
                return True

            if not (lower < curr.val < upper):
                return False

            left = checker(lower, curr.left, curr.val)
            right = checker(curr.val, curr.right, upper)

            return left and right

        return checker(float("-inf"), root, float("inf"))

    # Time complexity is O(N) we traverse all nodes
    # Space O(N) when the recursion stack N is H in a skewed tree