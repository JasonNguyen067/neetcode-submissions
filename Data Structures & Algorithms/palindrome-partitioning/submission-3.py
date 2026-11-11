class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        palindrome = []

        def palindromeChecker(left, right):
            while left < right:     
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def dfs(start):
            if start == len(s):
                result.append(palindrome.copy())
                return

            for end in range(start, len(s)):
                if palindromeChecker(start, end):
                    palindrome.append(s[start:end + 1])
                    
                    dfs(end + 1)
                    
                    palindrome.pop()

        dfs(0)

        return result
