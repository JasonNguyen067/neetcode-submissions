class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charCount = defaultdict(int)
        left = 0
        longest = 0

        for right in range(len(s)):
            charCount[s[right]] += 1
            while charCount[s[right]] > 1:
                charCount[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest