class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find 2 bars such that the min of their 2 heights * the distance 
        # between them produces the greatest value possible within the input array
        # invariant: because the volume is limited by the height of the lower bar
        # a greater height than the current can only be found by replacing the lower bar
        max = 0
        l = 0
        r = len(heights) - 1

        #  [1,7,2,5,4,7,3,6]
        #   0 1 2 3 4 5 6 7
        # max = 36
        # area = 36
        # 


        while l < r:
            # calc area and see if max should be replaced
            area = min(heights[l], heights[r]) * (r - l)
            if area > max:
                max = area
            
            # move inward from lower bar
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] == heights[r]:
                l += 1
                r -= 1

        return max  




         