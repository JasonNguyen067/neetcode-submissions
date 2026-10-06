class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one = 1
        two = 2

        for i in range(3, n + 1):
            curr = one + two
            one = two
            two = curr

        return two

    # Time complexity is o(N)
    # space O(1)