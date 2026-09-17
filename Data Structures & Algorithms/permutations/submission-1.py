class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutations = []
        used = [False] * len(nums)

        def dfs():
            if len(permutations) == len(nums):
                result.append(permutations.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                permutations.append(nums[i])
                used[i] = True

                dfs()

                permutations.pop()
                used[i] = False

        dfs()
        return result

        # Time complexity is O(2^n)
        # Space complexity is O(N)