class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        left = 0

        for right in range(len(prices)):
            if prices[right] - prices[left] > 0:
                price = max(price, prices[right] - prices[left]) 
            if prices[right] < prices[left]:
                left = right

        return price
