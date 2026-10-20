# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.checker(root, subRoot): # Because each recursive call will either pass the root.left or root.right for us
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        

    def checker(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        return self.checker(p.left, q.left) and self.checker(p.right, q.right)

    # Time comoplexity is O(M * N) for M nodes the side of N check because of subroot 
    # Space complexity is O(M + N) because the recursive stack call can get M deep + N calls deep for subroot