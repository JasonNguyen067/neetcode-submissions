class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = defaultdict(int)
        left = 0
        best = 0
        maxletter = 0

        for right in range(len(s)):
            letters[s[right]] += 1
            maxletter = max(maxletter, letters[s[right]])

            while (right - left + 1) - maxletter > k:
                letters[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best