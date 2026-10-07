class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for curAmount in range(1, amount + 1):
            for coin in coins:

                if curAmount - coin >= 0:
                    dp[curAmount] = min(dp[curAmount], 1 + dp[curAmount - coin])

        return dp[amount] if dp[amount] != float("inf") else -1