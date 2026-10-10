class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        removals = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if prevEnd > start:
                removals += 1
            else:
                prevEnd = end

        return removals

        # Time complexity is O(N)
        # Space complexity is O(1)