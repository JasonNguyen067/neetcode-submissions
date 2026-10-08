class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}

        for val in nums:
            nextdp = dp.copy()

            for currNum in dp:
                if currNum + val == target:
                    return True

                if currNum + val < target:
                    nextdp.add(currNum + val)

            dp = nextdp

        return False