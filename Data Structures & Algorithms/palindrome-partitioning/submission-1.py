class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start):
            if start == len(s):
                result.append(partition.copy())
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    partition.append(s[start: end + 1])

                    dfs(end + 1)

                    partition.pop()

        dfs(0)

        return result

        # Time complexity is O(N * 2^N) 
#         N-1 possible cut locations
#           each has 2 choices: cut / don't cut
#        → about 2^N partitions

#          each answer can take O(N) to copy
#          → O(N * 2^N) 
        # Space complexity is O(N) n calls deep 
