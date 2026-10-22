class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        values = self.values[key]
        right = len(values) - 1
        best = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                best = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return best