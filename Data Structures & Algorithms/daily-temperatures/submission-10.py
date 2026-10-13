class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Set a array to 0 by default, 
        # Track indexes so we can track the amount of days, but we will also need value to compare temps 

        # What about cases where two temps are equal that means set as i right

        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                result[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)

        return result