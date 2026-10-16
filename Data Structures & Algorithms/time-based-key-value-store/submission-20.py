class TimeMap:

    def __init__(self):
        self.timeHolder = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeHolder[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        listTraversal = self.timeHolder[key]
        left = 0
        right = len(listTraversal) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if listTraversal[mid][1] <= timestamp:
                result = listTraversal[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result 