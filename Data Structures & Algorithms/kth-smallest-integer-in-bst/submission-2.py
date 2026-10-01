# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right

        # Time complexity is O(N) in case where O(N) is skewed, doesnt matter if its skewed tho cuz it goes in order anyways for bst, but matters more then K so k is size of N 
        # Space compelxity is O(N) based of the stack like the whole stack be stored worst case O(N) aka.1 node/