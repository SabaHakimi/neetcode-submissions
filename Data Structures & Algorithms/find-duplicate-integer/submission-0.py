class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # searching for a duplicate
        # hashmap -> Nope O(1) space and O(n) time
        # no modifying array
        # each int in nums is in range [1, n] inclusive
        # no nums below 1, no nums greater than n
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return nums[i]
            else:
                visited.add(nums[i])