class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for val in nums:
            current_best = 1

            if val + 1 not in num_set:
                while val - 1 in num_set:
                    current_best += 1
                    val -= 1
            best = max(best, current_best)

        return best

        # time complexity is O(N)
        # space complexity is O(n)