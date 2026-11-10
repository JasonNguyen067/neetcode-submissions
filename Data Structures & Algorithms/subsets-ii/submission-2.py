class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        results = []
        combinations = []

        def dfs(i):
            if i == len(nums):
                results.append(combinations.copy())
                return

            combinations.append(nums[i])
            dfs(i + 1)

            combinations.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)

        return results
