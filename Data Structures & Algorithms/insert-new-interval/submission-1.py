class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                results.append(newInterval)
                return results + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                results.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]
        results.append(newInterval)
        return results

            # [1, 5], [2, 9]
            # Min of 1 and 2 at index 0 for both is 1 
            # max of 5 and 9 at index 1 for both is 9
            # [1, 9]

            # New Interval gets reused and appended and returned if theres values existing after merge
            # ELse if its last value append after for loopp done and return results
