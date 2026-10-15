class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            timeNeeded = 0

            for pile in piles:
                timeNeeded += math.ceil(pile / mid)

            if timeNeeded <= h:
                right = mid
            else:
                left = mid + 1

        return left

        # Time complexity is O(LOGN)
        # Space complexity is O(1)
            