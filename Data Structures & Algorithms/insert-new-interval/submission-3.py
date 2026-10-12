class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 3 cases, overlap one or the other or bot,
        # Insert before the other
        # insert before all

        # is [3, 5] and [5, 7] considered overlapping on the 5?

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

        # Time complexity is O(N)
        # Space O(N)

        #esentially algo is if list1 list2 list3

        # lets say list2 less than list 3 and list2 is the newinterval then we can just append everything after
        # after we append
        # other case is lets say list1 is less tan new interval just append list1
        # else if any overlap, merge the current index and increase bounds take the minimum of index 0 and 
        # max of index 1 of each list, and then reuse that interval by just updating newinterval directly
        # Then we can reusre it inthe comaprison 
