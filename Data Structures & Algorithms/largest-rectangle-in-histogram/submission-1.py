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
            max_area = max(max_area, width * height)

        return max_area

        # Even though a single iteration may pop many elements, 
        # each element can only be pushed once and popped once 
        # over the entire execution. Therefore the total number of stack 
        # operations is O(N), giving an overall time complexity of O(N).
        # Space complexity O(N) for the entire stack containing N values inside of it 
