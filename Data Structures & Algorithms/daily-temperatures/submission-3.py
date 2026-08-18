class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Work with index and value for this 
        stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                result[stack[-1]] = index - stack[-1]
                stack.pop()
            else:   
                stack.append(index)
        return result