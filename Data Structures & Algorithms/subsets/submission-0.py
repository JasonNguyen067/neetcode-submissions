class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        subset = []

        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)


        dfs(0)
        return result


# Time: O(N * 2^N)
# There are 2^N possible subsets because each of the N elements
# has 2 choices: take it or skip it.
# At each completed subset, subset.copy() can copy up to N elements,
# so total time is O(N * 2^N).

# Space: O(N) auxiliary space.
# The recursion stack can go at most N levels deep,
# and the current subset can contain at most N elements.

# Base case:
# if i == len(nums)
# For nums = [1,2,3], len(nums) = 3 and valid indices are 0,1,2.
# When dfs(3) is called, we've made a take/skip decision for every element,
# so we save the current subset and return.