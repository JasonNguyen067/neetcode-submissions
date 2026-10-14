class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        bestLeft = 0
        bestRight = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                bestLeft = max(bestLeft, height[left])
                water += bestLeft - height[left]
                left += 1
            else:
                bestRight = max(bestRight, height[right])
                water += bestRight - height[right]
                right -= 1 

        return water

        # Time complexity is O(N)
        # Space complexity O(1)