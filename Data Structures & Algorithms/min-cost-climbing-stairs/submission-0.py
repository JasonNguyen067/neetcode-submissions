class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[0]
        two = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(one, two)
            one = two
            two = curr

        return min(one, two)

        # Time complexity is o(N)
        # Space complexity is o(1)