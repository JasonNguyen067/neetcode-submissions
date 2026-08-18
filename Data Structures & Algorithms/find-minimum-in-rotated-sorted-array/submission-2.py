class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1 

        return nums[left]

        # Time complexity is O(LOGN) cuts search space in half
        # Space complexity is O(1)
