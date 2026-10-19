# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We want to go for a breadth first search algorithm going level by level
        # In each one we want to have a prospective queue in when we start to being able ot 
        # find the next nodes we want to do work on
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            currLength = len(queue)
            level = []
            for _ in range(currLength):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

        # Time complexity is O(N) for n nodes we traverse
        # Space is O(N) for n nodes stored in result