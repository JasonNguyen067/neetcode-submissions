class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                max_area = max(max_area, width * height)
                start = index

            stack.append((start, h))

        for index, height in stack:
            width = len(heights) - index
            max_area = max(max_area, height * width)

        return max_area

        # Time complexity O(N^2) via stack and stuff keeps getting popped and lower and lower h's  but thats 1 add 1 sub
        # Space complexity is O(N)