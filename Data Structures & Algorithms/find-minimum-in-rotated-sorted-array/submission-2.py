class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        l = 0
        r = length - 1

        if nums[l] < nums[r]:
            return nums[0]

        while (r - l) >= 1:
            r_mid = l + (r - l) // 2 + 1
            l_mid = r_mid - 1
            print("l_mid:", l_mid)
            print("r_mid:", r_mid)
            if nums[r_mid] < nums[l_mid]:
                return nums[r_mid]
            if nums[l] > nums[l_mid]:
                r = l_mid
                print("r", r)
                print("l", l)
            elif nums[r] < nums[r_mid]:
                l = r_mid
                print("r", r)
                print("l", l)
            print("r - l:", r - l)

    # 4, 5, 0, 1, 2, 3
    # 0, 1, 2, 3, 4, 5
    # l = 0 
    # r = 5 -> 2
    # l_mid = 2
    # r_mid = 3
    #        
    #  7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6,
    #  0, 1, 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13 14 15 16 17 18
    #  l = 10 
    #  r = 14
    #  r_mid = 13 
    #  l_mid = 12  

    # binary search
    # repeat until found min
        # start at middle
        # compare left and right
        # set search bounds to be within the smaller 'half'

        