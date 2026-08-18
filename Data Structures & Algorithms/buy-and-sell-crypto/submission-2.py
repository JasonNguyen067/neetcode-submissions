class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_price = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                max_price = max(max_price, prices[right] - prices[left])

        return max_price
        