class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # build a set
        # iterate over the set:
        #    skip all elements for which a previous exists
        #    for each valid element, count how long of a consecutive interval it is, 
        # eventually returning the max
        
        set_nums = set(nums)
        longest_consec = 0

        # iterate set
        for num in set_nums:
            # if a prev doesn't exist
            if num - 1 not in set_nums:
                current_consec = 1
                neighbor = num + 1
                while neighbor in set_nums:
                    current_consec += 1
                    neighbor += 1
                if current_consec > longest_consec:
                    longest_consec = current_consec
        
        return longest_consec
