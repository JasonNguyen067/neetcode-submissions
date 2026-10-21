class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotation is i + whatever
        # we don't know the exact value we are looking for so we won't do a equal signcomparison

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
                
        return nums[left]

        # Time complexity is O(LOGN)
        # Space O(1)