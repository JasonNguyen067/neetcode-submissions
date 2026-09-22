"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        adjacency = {}

        def dfs(curr):
            if curr in adjacency:
                return adjacency[curr]

            copy = Node(curr.val)
            adjacency[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy
                

        return dfs(node)

        # Time complexity is O(V + E) 
        # Space complexity is O(V) 
        # “Time complexity is O(V + E) because we visit each vertex once and iterate through each edge in the neighbor lists. Space complexity is O(V) for the original-to-copy hashmap and the recursion call stack in the worst case.”