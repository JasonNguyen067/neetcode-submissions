class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        CharacterDictionary = defaultdict(int)
        ChDict2 = defaultdict(int)
        left = 0
        
        for letter in s1:
            CharacterDictionary[letter] += 1

        for right in range(len(s2)):
            ChDict2[s2[right]] += 1

            while (right - left) + 1 > len(s1):
                ChDict2[s2[left]] -= 1
                if ChDict2[s2[left]] == 0:
                    del ChDict2[s2[left]]
                left += 1

            if CharacterDictionary == ChDict2:
                return True

        return False