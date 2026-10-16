class TimeMap:

    # we know that timestamps of set are strictly increasing, we don't need any special technique to append in order
    # for a specific val

    def __init__(self):
        self.timeHolder = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeHolder[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        left = 0
        values = self.timeHolder[key]
        right = len(values) - 1
        
        # We do left <= right because we want to be able to compare all values
        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                left = mid + 1
                # get current best val
            else:
                right = mid - 1

        return result

