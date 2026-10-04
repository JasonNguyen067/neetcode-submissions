# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Preorder traversal
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return

            result.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if values[i] == "N":
                i += 1
                return None

            root = TreeNode(int(values[i]))
            i += 1

            root.left = dfs()
            root.right = dfs()

            return root 

        return dfs()

        # Time compolexityis O(N)
        # Space complexty is O(N)
        