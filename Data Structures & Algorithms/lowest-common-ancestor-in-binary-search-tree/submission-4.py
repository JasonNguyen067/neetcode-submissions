# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Since this is a binary search tree we know the following conditions are true
        # In the scenario where both are smaller, it must be to the left, as smaller childs are on the left
        # in bst, while both are larger then it must be to the right as bigger childs are on the right
        # in the case where both nodes don't follow the condition, its not possible to further iterate
        # to either side. This is how we know that we are at the LCA

        # Following uqestions, can root be empty, and are we guaranteed an answer?

        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current

        # Time complexity is O(N) worst case its a skewed one
        # Space complexity is just O(1)