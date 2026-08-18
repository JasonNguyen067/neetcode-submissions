class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = nums1 + nums2
        totallength = len(total)
        half = totallength // 2

        total.sort()

        if totallength % 2 == 0:
            return (total[half - 1] + total[half]) / 2
        
        return total[half]