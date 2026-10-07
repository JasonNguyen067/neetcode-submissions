class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0


        def checker(l, r):

            answer = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1
                answer += 1

            return answer

        for i in range(len(s)):
            res += checker(i, i)
            res += checker(i, i + 1)

        return res