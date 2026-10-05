class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for crs, prereq in prerequisites:
            graph[prereq].append(crs)

        state = [0] * numCourses

        order = []

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1

            for nextcourse in graph[course]:
                if not dfs(nextcourse):
                    return False
                
            order.append(course)
            state[course] = 2

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return order[::-1]