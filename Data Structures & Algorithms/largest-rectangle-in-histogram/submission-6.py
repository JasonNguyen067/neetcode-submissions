class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # We want a way to best calculate cases of best width * height scenario like 2x4 
        # But then also singular casese like 7 X 1
        # And any left over cases
        # Keep a stack and a best counter

        # While we have a stack and the next height is lower, no longer posisble calculate best height from there
        # so like 6 x 2 then a 5 comes in calculate teh 12 right there then append back a 5 at index 0 
        # so we can do a 5 x 3 

        stack = []
        best_val = 0

        for index, height in enumerate(heights):
            start = index

            while stack and stack[-1][1] > height:
                idx, ht = stack.pop()
                width = index - idx
                best_val = max(best_val, width * ht)
                start = idx

            stack.append((start, height))


        # Left over case
        for idx, height in stack:
            width = len(heights) - idx
            best_val = max(best_val, width * height)

        return best_val

        # Time complexity is O(N) N stack push pop
        # Space complexity is O(N) N stored