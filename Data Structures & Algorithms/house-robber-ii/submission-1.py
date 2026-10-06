class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(arr):
            one = 0
            two = 0

            for i in range(len(arr)):
                curr = max(one + arr[i], two)
                one = two
                two = curr

            return two

        return max(helper(nums[1:]), helper(nums[:-1]))

        # Time complexity is O(N)
        # Space complexity is O(1)