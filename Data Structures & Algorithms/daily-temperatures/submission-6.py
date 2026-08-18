class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        # This defaults it to 0 in case of no warmer temperature


        for index, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                results[stack[-1]] = index - stack[-1]
                stack.pop()

            stack.append(index)
            # Want to append indexes, can track day difference

        # Time complexity is O(N) one pass through array 
        # space complexity is O(N) worst case place entire stack
    
        return results