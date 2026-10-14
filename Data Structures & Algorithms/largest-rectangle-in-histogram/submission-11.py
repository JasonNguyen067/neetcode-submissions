class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # conditions if meet a smaller height, pop and then calcualte the width and height before the lower number
        # like 2 x 4 then you meet a 1 
        # but then you can also reappend the furthest left index of the calculation and then set a height of 1
        # to remultiply
        # Then there are cases where theres never a actual small number to the right of whatever curr and index was appended
        # Then those can be cleaned up on a clean algorithm later on 
        

        result = []
        best = 0
        
        for index, height in enumerate(heights):
            curr = index
            
            while result and result[-1][1] > height:
                curr, hgt = result.pop()
                width = index - curr
                best = max(best, width * hgt)
            
            result.append((curr, height))

        for index, height in result:
            width = len(heights) - index
            best = max(best, width * height)

        return best

        # Time complexity is O(N)
        # Space complexity is O(N)