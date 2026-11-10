class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for val in stones:
            heapq.heappush(heap, -val)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x < y:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0

        # Time complexity O(LOGN) 
        # Space O(N)