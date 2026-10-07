class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for val in nums[1:]:
            if val < 0:
                curMax, curMin = curMin, curMax

            curMax = max(val, curMax * val)
            curMin = min(val, curMin * val)

            res = max(res, curMax)

        return res

        # Time complexity is O(N)
        # Space complexity is O(1)