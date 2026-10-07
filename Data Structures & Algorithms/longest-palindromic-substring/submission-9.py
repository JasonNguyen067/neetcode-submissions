class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def checker(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r] #cuz l forward one cuz of invalid range, and r is exclusive of its val in slice

        for i in range(len(s)):
            answer1 = checker(i, i)
            answer2 = checker(i, i + 1)

            if len(answer1) > len(res):
                res = answer1
            
            if len(answer2) > len(res):
                res = answer2
            
        return res