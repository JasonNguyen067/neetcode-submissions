class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0


        for num in num_set:

            if num - 1 not in num_set:
                length = 1

                while num + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest

        # Time complexity is O(N)
        # Space complexity is O(N)

        # One pass through array for time
        # One set stored with n nums for space