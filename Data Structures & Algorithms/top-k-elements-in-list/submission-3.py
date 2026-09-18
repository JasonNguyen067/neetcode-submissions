class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dictItems = defaultdict(int)

        for val in nums:
            dictItems[val] += 1


        buckets = [[] for _ in range(len(nums) + 1)]

        for name, freq in dictItems.items():
            buckets[freq].append(name)

        for i in range(len(buckets) - 1, -1, -1):
            if len(result) == k:
                return result
            for val in buckets[i]:
                result.append(val)

