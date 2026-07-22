class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table_of_entries = {}
        for num in nums:
            if num in table_of_entries: 
                return True 
            table_of_entries[num] = 1
        return False
