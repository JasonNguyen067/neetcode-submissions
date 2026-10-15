class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        window = defaultdict(int)

        for letter in t:
            need[letter] += 1

        res = ""
        resLen = float("inf")
        needCount = len(need)
        have = 0
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == needCount:
                if (right - left + 1) < resLen:
                    res = s[left:right + 1]
                    resLen = len(res)

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        return res

        # Time complexity is O(N)
        # Space O(N) worst case the result string stores the entire substring