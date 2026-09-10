# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        current = root

        while current:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right

        return root

        # Time complexity is O(N) worst case when skewed 
        # Space complexity is O(1) simple operations like create node or current = current.right


        # If root doesn't exist create node there,
        # Else literally simple while loop check
        # Check val and its a BST so iteratively, if it doesnt exist create!