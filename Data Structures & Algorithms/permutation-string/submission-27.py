class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        firstCount = defaultdict(int)
        secondCount = defaultdict(int)
        left = 0

        for val in s1:
            firstCount[val] += 1


        for right in range(len(s2)):
            secondCount[s2[right]] += 1

            while right - left + 1 > len(s1):
                secondCount[s2[left]] -= 1

                if secondCount[s2[left]] == 0:
                    del secondCount[s2[left]]

                left += 1

            if firstCount == secondCount:
                return True

        return False 