class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = defaultdict(int)

        for val in nums:
            values[val] += 1

    

        buckets = [[] for _ in range(len(nums) + 1)]

        results = []

        for val, freq in values.items():
            buckets[freq].append(val)

        for i in range(len(buckets) - 1, -1, -1):
            for val in buckets[i]:
                results.append(val)

                if len(results) == k:
                    return results
