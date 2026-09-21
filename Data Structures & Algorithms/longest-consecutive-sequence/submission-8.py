class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        max_length = 0

        for val in nums:
            curr_best = 1
            if val + 1 not in num_sets:    
                while val - 1 in num_sets:
                    curr_best += 1
                    val = val - 1
                max_length = max(max_length, curr_best)
        return max_length
        