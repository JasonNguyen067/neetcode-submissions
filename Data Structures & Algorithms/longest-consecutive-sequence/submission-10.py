class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        max_length = 0

        for val in nums:
            current_best = 1
            if val + 1 not in num_sets:
                while val - 1 in num_sets:
                    current_best += 1
                    val = val - 1
                
            max_length = max(max_length, current_best)

        return max_length
        
        # Time complexity is O(N)
        # SPace is O(N)