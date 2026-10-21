class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.values[key]) - 1
        currVal = self.values[key]
        best = ""

        while left <= right:
            mid = (left + right) // 2

            if currVal[mid][1] <= timestamp:
                best = currVal[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return best    
