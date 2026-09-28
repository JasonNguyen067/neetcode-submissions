class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best_container = 0

        # Questions for interviewer,
        # Is there a Null string
        # Is there a empty string
        # Are we guaranteed an answer

        while left < right:
            width = right - left
            height = min(heights[left], heights[right]) # take the minimum of the two, to multiply cuz itll fit
            size = width * height
            best_container = max(best_container, size)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
           

        return best_container
