from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            counter = [0] * 26
            for letter in word:
                counter[ord(letter) - ord('a')] += 1
            result[tuple(counter)].append(word)

        return list(result.values())