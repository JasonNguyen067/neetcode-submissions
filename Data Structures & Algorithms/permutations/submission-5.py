class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        combinations = []
        used = [False] * len(nums)

        def dfs():
            if len(combinations) == len(nums):
                result.append(combinations.copy())
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue

                combinations.append(nums[i])
                used[i] = True

                dfs()

                combinations.pop()
                used[i] = False

        dfs()
        return result

