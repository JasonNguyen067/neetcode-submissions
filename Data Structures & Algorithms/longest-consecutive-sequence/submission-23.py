class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        biggest_number = 0

        for i in range(len(nums)):
            streak = 1
            val = nums[i]

            if val + 1 in num_set:
                continue

            while (val - 1) in num_set:
                val -= 1
                streak += 1
                
            biggest_number = max(biggest_number, streak)

        return biggest_number

        # Time complexity is O(N)
        # Space complexity is O(N)
