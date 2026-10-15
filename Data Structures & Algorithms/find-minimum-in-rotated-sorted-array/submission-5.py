class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Rotation is whatever index is incremented + I indexes
        # We don't have a specific comparison or know the specific value we are looking for,
        # All we know is that we want to find a minimum value, which means convergence
        # In convergence we will have a while loop that is just while left < right itll slowly close on the location
        # based off our conditions, and then we can return the left pointer which is going to have 


        # Assume unqiue 

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]

        # If sorted fromn mid to right take mids value cuz thats the lowest in that sequence

        # Else we know mid is higher than right, we dont want mid and somewhere right is probably lower
        # SO we take one value past mid closing the range and trying to find a smaller value because we 
        # Know its somewhere on that right side
        # Eventually our left pointer will converge and left will have the lowest val so we return left

        [3, 4, 5, 6, 1, 2]

        # 0 + 5 // 2 is 2

        # index 2 greater than index 5 so the else
        # left becomes index 3 
        # next case left is 3, right is 5 
        # 1 is less than or equal to 2 
        # right = index 4 
        # mid is 3 
        # 6 is greater than 1 so left = mid + 1 so index 3 + 1 is index 4 
        # left == right
        # index 4 == 4 so return left