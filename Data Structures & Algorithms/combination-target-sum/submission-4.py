class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combinations = []

        def dfs(i, total):
            if total == target:
                result.append(combinations.copy())
                return
            if i >= len(nums) or total > target:
                return

            combinations.append(nums[i])
            dfs(i, total + nums[i])

            combinations.pop()

            dfs(i + 1, total)

        dfs(0, 0)

        return result