class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for val in num_set:
            curr = val
            best = 1
            if val - 1 in num_set:
                continue
            
            while curr + 1 in num_set:
                curr += 1
                best += 1
                
            longest = max(longest, best)

        return longest

        # Time complexity is O(N) one pass
        # Space complexity O(N) cuz of numset
