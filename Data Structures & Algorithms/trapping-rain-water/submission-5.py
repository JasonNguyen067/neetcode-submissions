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

        # One pass time complexity O(N)
        # Space complexity O(1) just pointers left right and then vars like water max left max right
        