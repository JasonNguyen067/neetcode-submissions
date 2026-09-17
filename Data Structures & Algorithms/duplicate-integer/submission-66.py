class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Answers = set()

        for val in nums:
            if val in Answers:
                return True
            Answers.add(val)
        return False

        # Space O(N)
        # Time O(N)
            