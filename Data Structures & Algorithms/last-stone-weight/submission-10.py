class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        values = [-stone for stone in stones]
        heapq.heapify(values)

        while len(values) > 1:
            x = -heapq.heappop(values)
            y = -heapq.heappop(values)

            if x < y:
                heapq.heappush(values, -(y - x))
            elif x > y:
                heapq.heappush(values, -(x - y))

        return -values[0] if values else 0