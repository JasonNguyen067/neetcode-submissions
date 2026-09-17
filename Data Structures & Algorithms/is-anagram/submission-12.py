class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = [0] * 26
        counter2 = [0] * 26

        for val in s:
            counter1[ord(val) - ord('a')] += 1

        for val in t:
            counter2[ord(val) - ord('a')] += 1

        if counter1 == counter2:
            return True
        return False

        # Time complexity is O(n) 
        # Space complexity O(1) for 26 letters