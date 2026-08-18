class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First set an array that has the value before it to not include itself
        # Like the prefix then pass through one with the suffix not including itself
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

        # Time complexity is o(N)
        # Space complexity O(1) extra space