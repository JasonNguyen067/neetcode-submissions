class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combinations = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                result.append(combinations.copy())
                return

            if i >= len(candidates) or total > target:
                return

            combinations.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            combinations.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, total)

        dfs(0, 0)

        return result