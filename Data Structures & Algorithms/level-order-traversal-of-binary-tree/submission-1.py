# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # For this solution binary tree level order traversal essentially means we do it level by level
        # We will go with bfs, how will we do it? level based queues

        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            l_size = len(queue)
            level = []

            for _ in range(l_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

        # Time complexity is O(N)
        # Spcae cokmpelxity is o(N)