class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()

        def dfs(r, c):
            
            if (r < 0 or r >= rows or
            c < 0 or c >= cols or 
            (r, c) in visited or
            grid[r][c] != "1"):
                return False

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return True

        # Have a rows, 
        # have a cols 
        # have a visited check
        # have a islands variable that I increment
        # have a dfs function with a validity check
        # validity will include col bound, row bound, visited before, and if its a 1, aka valid.

        # then have a inner call, 

        # after all the visit functions do I have a visited remove?


        # if valid return a += 1? 

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c):
                    islands += 1

        return islands