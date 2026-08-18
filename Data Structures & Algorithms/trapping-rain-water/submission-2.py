class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        max_left = 0
        max_right = 0


        while left < right:

            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                water += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                water += max_right - height[right]
                right -= 1

        return water

        # Time complexity is O(N) one pass through the array
        # Space complexity is O(1) just allocated to pointers left right and storage water

