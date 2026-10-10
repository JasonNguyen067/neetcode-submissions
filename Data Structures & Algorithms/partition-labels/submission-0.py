class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        result = []
        currMax = 0
        left = 0

        for i in range(len(s)):
            currMax = max(currMax, last[s[i]])

            if i == currMax:
                result.append(i - left + 1)
                left = i + 1

        return result