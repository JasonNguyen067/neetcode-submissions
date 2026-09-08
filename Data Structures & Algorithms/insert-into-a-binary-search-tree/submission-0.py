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

        # Time complexity is O(LOGN) cuz bst cuts search in half
        # Space complexity O(1) one insert  and the roots = root.left or riot.right
