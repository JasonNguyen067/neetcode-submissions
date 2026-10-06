class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        firstdict = defaultdict(int)
        for val in s1:
            firstdict[val] += 1

        seconddict = defaultdict(int)

        left = 0

        for right in range(len(s2)):
            seconddict[s2[right]] += 1

            while right - left + 1 > len(s1):
                seconddict[s2[left]] -= 1

                if seconddict[s2[left]] == 0:
                    del seconddict[s2[left]]

                left += 1

            if firstdict == seconddict:
                return True

        return False