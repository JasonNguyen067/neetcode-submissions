class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        while left < len(prices) - 1:
            for right in range(left + 1, len(prices)):
                best = prices[right] - prices[left]
                if best > 0:
                    profit = max(profit, best)
            left += 1
        return profit
