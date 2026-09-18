class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index, cur):
            if index == len(digits):
                res.append(cur)
                return

            for c in digitToChar[digits[index]]:
                backtrack(index + 1, cur + c)

        if digits:
            backtrack(0, "")

        return res

        # Time complexity O(N * 4^N) 4^n being worst case theres wxyz N being n iterations for digits
        # Space complexity is O(N) for call; stack and combinationms

