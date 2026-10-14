class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needDict = defaultdict(int)
        haveDict = defaultdict(int)

        for letter in t:
            needDict[letter] += 1

        res = ""
        reslen = float("inf")
        left = 0
        needCount = len(needDict)
        have = 0

        for right in range(len(s)):
            haveDict[s[right]] += 1

            if s[right] in needDict and haveDict[s[right]] == needDict[s[right]]:
                have += 1

            while have == needCount:
                if right - left + 1 < reslen:
                    res = s[left:right + 1]
                    reslen = len(res)

                haveDict[s[left]] -= 1
                
                if s[left] in needDict and haveDict[s[left]] < needDict[s[left]]:
                    have -= 1
                
                left += 1

        return res

        # Time complexity O(N) one pass

        # Space complexity O(1) just letter increments 