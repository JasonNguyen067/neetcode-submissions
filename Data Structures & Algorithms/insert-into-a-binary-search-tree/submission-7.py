# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Guaranteed an answer because new value does nto exist int he orginal bst
        # I see that root is optional, in that case what happemns hwen root doesnt exist?
        # Well I assume we just create a node.
        # and then the case is if val is greater than the current node and the rigth node doesnt exist 
        # Create a treenode on right side, else if less than the current node and lef tnode doesnt exist
        # then createa. treenode else go down further left

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

        # Return root as it contains the new tree

        # Time compelxity is O(N) worst case skewed and we have to visit the whole tree
        # Space compelxity is O(1) for one node created