# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Single result list answer
        # Want to only append node.val when its index len(level) - 1 
        # Also want to do it level by level so we will go with the breadth first search algorithm

        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            queueLen = len(queue) - 1
            for i in range(len(queue)):
                node = queue.popleft()

                if i == queueLen:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result

        # Time complexity is O(N) we traverse N Nodes
        # Space O(N) worst case its right skewed and N nodes gets stored in result    