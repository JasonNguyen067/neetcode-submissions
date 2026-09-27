# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            if left == -1:
                return -1

            right = dfs(curr.right)
            if right == -1:
                return -1

            if check(left, right) == False:
                return -1

            return max(left, right) + 1

        def check(left, right):
            if left > right:
                if left > right + 1:
                    return False
                return True
            else:
                if right > left + 1:
                    return False
                return True

        return dfs(root) != -1
                
