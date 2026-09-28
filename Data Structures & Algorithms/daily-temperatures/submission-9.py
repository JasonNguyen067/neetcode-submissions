class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                result[stack[-1]] = index - stack[-1]
                stack.pop()
            else:
                stack.append(index)

        return result


        # We want comparisons, if current day is higher than a index day temp then have while loop that check
        # pops and modifies result inplace, also we want stack to store indexes
        # We want index and temperature, index tracks the current day temp is temp

        # Time complexity is O(N)
        # Space complexity is O(N)