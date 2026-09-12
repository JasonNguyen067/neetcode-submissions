"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def build(r, c, size):
            first = grid[r][c]
            same = True

            for row in range(r, r + size):
                for col in range(c, c + size):
                    if grid[row][col] != first:
                        same = False
                        break

                if not same:
                    break

            if same:
                return Node(first == 1, True)

            half = size // 2

            top_left = build(r, c, half)
            top_right = build(r, c + half, half)
            bot_left = build(r + half, c, half)
            bot_right = build(r + half, c + half, half)

            return Node(
                True,
                False,
                top_left,
                top_right,
                bot_left,
                bot_right
            )


        return build(0, 0, n)