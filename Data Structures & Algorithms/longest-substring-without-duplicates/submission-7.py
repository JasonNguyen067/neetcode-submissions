class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = defaultdict(int)
        left = 0
        best = 0

        for right in range(len(s)):
            letters[s[right]] += 1

            while letters[s[right]] > 1:
                letters[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best