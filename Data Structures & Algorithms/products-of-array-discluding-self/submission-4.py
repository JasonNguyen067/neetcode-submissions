class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

        # Time complexity is O(N)
        # Space complexity is O(N)
            