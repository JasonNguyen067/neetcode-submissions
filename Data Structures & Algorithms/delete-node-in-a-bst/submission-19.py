# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # In the case where we delete a node what do we want to return in a bst?
        # First case is if node.right exists then we return that because we want teh closest higher val
        # Else return node.left if that exists
        # else if both lef tand right exist og right and traverse down furthest left for the current closest
        # val to our current node

        # Lets go with a dfs recursive solution

        # I see a case where there is no roo t
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            successor = root.right

            while successor.left:
                successor = successor.left

            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)

        return root
