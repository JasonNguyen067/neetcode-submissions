class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(r, c):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != "1" or (nr, nc) in visited):
                    continue

                dfs(nr, nc)

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands

        # Esentially mapping what we've visited and the connected things inside of the dfs call onto visited
        # Us making the call itself allows us to believe that its unique, along with 1 count of the current island