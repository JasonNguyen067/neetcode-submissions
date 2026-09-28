class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            leftval = numbers[left]
            rightval = numbers[right]
            total = leftval + rightval
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]


    # Auxilary or extra space the same, space not including the output