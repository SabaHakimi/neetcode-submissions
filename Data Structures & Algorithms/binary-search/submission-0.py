class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search for O(logn)
        # pick midpoint
        # if val == target, return idx
        # if val > target, search to left of val
        # if val < target, search to right of val
        l = 0
        r = len(nums) - 1
        while l <= r: # come back to this
            mid_point = r + l // 2 # need to account for defaulting to going left
            if nums[mid_point] == target:
                return mid_point
            elif nums[mid_point] > target:
                # search left
                r = mid_point - 1
            elif nums[mid_point] < target:
                # search right
                l = mid_point + 1
        
        return -1


    