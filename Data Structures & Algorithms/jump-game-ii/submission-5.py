class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        furthest = 0
        currentend = 0

        for i in range(len(nums) - 1): # This is because we dont want to include the last index unnec xtra jump
            furthest = max(furthest, nums[i] + i)

            if i == currentend:
                jumps += 1
                currentend = furthest

        return jumps