class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing = [0] * (n + 1)
        incoming = [0] * (n + 1)

        for person, trusted_person in trust:
            outgoing[person] += 1
            incoming[trusted_person] += 1

        for person in range(1, n + 1):
            if incoming[person] == n - 1 and outgoing[person] == 0:
                return person

        return -1


        # Time complexity is O(N) for the loops
        # Space complexity is O(N) for N stores in incoming and outgoing