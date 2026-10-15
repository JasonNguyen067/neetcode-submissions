class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # This one we have a target to compare to 
        # If target is not in there return -1 
        # We can return early and we need a direct comparison so we will use mid and use all indexes including
        # if left == right case so we will have a while loop left <= right
        # And we need to return the index if target equals to nums[mid] so we will return mid

        # SO two cases if mid is sorted with the right side and target is between that
        # So if it is sorted check if its between the sorted side, if not then look on the right side

        # Also assume unique values

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                
        return -1

        # Time complexity O(LOGN)
        # Space complexity o(1)
