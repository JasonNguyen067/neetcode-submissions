class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortedQueries = sorted(queries)

        heap = []
        answers = {}
        i = 0

        for query in sortedQueries:

            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                answers[query] = heap[0][0]
            else:
                answers[query] = -1

        return [answers[q] for q in queries]
        