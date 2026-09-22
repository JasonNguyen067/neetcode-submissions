class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = deque()
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if (nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        grid[nr][nc] != 1):
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

            minutes += 1

        if fresh == 0:
            return minutes

        return -1

        # Time complexity is O(M * N)
        # Space complexity is O(M * N) worst case whole shit is rotten and stored in teh deque with 1 fresh
