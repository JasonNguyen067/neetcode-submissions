class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # For something like this we are going to have to sort
        # Then have an array dedicated to the answer

        # Three pointesr one is left one is left +1. which clsoes in and then one is right which can also move inwards

        nums.sort()
        answer = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    # cuz we have to check the left < right case as we are forgettign duplicates 
                    # because the while case means we will go back to it so we have to check each adn everytime

                    # lets say we got s[left] and then finished appended and then appended one on the case right after that
                    # then we move it forward and it should be good wait but woudlnt it still be one too late 

                    # anyways adn thenw e push it forward a left and a right so that gets rid of it                     
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return answer


                    