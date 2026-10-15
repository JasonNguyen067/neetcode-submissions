class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hoursNeeded = 0

            for pile in piles:
                hoursNeeded += math.ceil(pile / mid)

            if hoursNeeded > h:
                left = mid + 1
            else:
                right = mid

        return left
        
        # Time complexity is O(LOGN)
        # SPace complexity is O(1)