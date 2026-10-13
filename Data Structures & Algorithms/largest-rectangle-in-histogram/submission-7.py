class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # When I look at this problem I think of a couple cases
        # How can I get the current best height if it is lets say a index has a heights[index] value of 20
        # How can I get the good ranges in between like 2 x 4 height col even if theres a 7 in between that
        # We should also be able to reappend to the stack of lower cases as we go if they are in succession
        # So lets say a height of 3 then 3 then 2 well then once it hits 2 since it gets lower pop, but then 
        # we can still reappend the 2 x 3 for later use

        stack = []
        best = 0

        for index, val in enumerate(heights):
            curr = index

            while stack and stack[-1][1] > val:
                idx, value = stack.pop()
                curr = idx
                rectangle = value * (index - curr)
                best = max(best, rectangle)

            stack.append((curr, val))

        for idx, val in stack:
            width = len(heights) - idx
            best = max(best, width * val)

        return best

        # Time complexity is O(N)
        # Space compelxity is O(N)
            