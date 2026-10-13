class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for val in num_set:
            curr = val
            best = 1

            if val - 1 in num_set:
                continue
            # This is so we can get to the lowest value of the sequence

            while curr + 1 in num_set:
                best += 1
                curr += 1

            longest = max(longest, best)

        return longest

        # Time complexity is O(N) for n passes in the loop
        # Space complexity is O(N) for the set