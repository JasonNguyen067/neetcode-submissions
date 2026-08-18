class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0    
        characterTracker = defaultdict(int)

        countTracker = defaultdict(int)

        for val in s1:
            countTracker[val] += 1

        for right in range(len(s2)):
            characterTracker[s2[right]] += 1

            while (right - left + 1) > len(s1):
                characterTracker[s2[left]] -= 1
                if characterTracker[s2[left]] == 0:
                    del characterTracker[s2[left]]
                left += 1

            if countTracker == characterTracker:
                return True

        return False