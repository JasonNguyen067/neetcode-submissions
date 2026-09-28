class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # outer loop condition should be 

        nums.sort()
        answers = []
        # 3 pointers left = i + 1 i is going to be the left left right is going to be len(nums) - 1
        
        for i in range(len(nums)):
            # duplicate check
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    answers.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return answers
            