class TimeMap:

    def __init__(self):
        self.storage = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []

        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""

        items = self.storage[key]
        left = 0
        right = len(items) - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2

            if items[mid][1] <= timestamp:
                answer = items[mid][0]
                left = mid + 1
            elif items[mid][1] > timestamp:
                right = mid - 1
        return answer

            
