class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}

        for i, char in enumerate(order):
            rank[char] = i



        for i in range(len(words) - 1):
            words1 = words[i]
            words2 = words[i + 1]

            min_len = min(len(words1), len(words2))

            for j in range(min_len):

                if words1[j] != words2[j]:
                    if rank[words1[j]] > rank[words2[j]]:
                        return False

                    break
            else:
                if len(words1) > len(words2):
                    return False

        return True

        # Time complexity O(N * M) n letters m words
        # space O(1)