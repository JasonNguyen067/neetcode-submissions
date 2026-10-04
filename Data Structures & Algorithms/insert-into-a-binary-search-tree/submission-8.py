# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Remember binary search tree, less than node is on eft, more than node on right
        # We can go with a simple iterative approach, if theres no node create Treenode and return
        # If there is a node to traverse if val is less than a current node, traverse down the left child
        # If there is a node to traverse and val is larger than a current node, traverse right child
        # Case of insertion is if the node to the right or left of a current node doesnt exist based off its
        # boolean logic

        if not root:
            return TreeNode(val)

        current = root 

        while current:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left
            elif val > current.val:
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right

        return root