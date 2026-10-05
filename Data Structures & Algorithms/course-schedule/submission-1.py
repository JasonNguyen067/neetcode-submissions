class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for crs, prereq in prerequisites:
            graph[prereq].append(crs)

        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1

            for nextCrs in graph[course]:
                if not dfs(nextCrs):
                    return False
            
            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

        # Time complexity is O(N) for N courses we cycle through
        # Space complexity is O(N) for N courses we store in the graph 
        