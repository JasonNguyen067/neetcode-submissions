class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        window = defaultdict(int)

        for val in t:
            need[val] += 1

        have = 0
        need_count = len(need)
        left = 0
        res_len = float("inf")
        res = ""

        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == need_count:
                if right - left + 1 < res_len:
                    res = s[left:right + 1]
                    res_len = len(res)

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                    
                left += 1

        return res


