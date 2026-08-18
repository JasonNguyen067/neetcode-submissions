class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_counter = defaultdict(int)

        mostFreqChar = float("-inf")
        longest = float("-inf")
        left = 0

        for right in range(len(s)):
            letter_counter[s[right]] += 1
            mostFreqChar = max(mostFreqChar, letter_counter[s[right]])

            while (right - left) + 1 - mostFreqChar > k:
                letter_counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1) 

        return longest

        # Time complexity is O(N)
        # space complexity is O(1)            
