# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            queue_length = len(queue) - 1
            for i in range(len(queue)):
                node = queue.popleft()
                if i == queue_length:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

        # Time complexity is O(N) worst case whole tree is processed which will happen in bfs
        # Space complexity is O(N) worst case right skewed
