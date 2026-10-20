class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        window = defaultdict(int)

        for letter in t:
            need[letter] += 1

        needCount = len(need)
        have = 0
        res = ""
        resultLength = float("inf")
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == needCount: # have best case now lets shrink the window
                if right - left + 1 < resultLength:
                    res = s[left: right + 1]
                    resultLength = right - left + 1

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        return res