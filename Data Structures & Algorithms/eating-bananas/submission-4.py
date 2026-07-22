class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

   
        # search space: eating rate, find min
        # min value is 1 hour. max value is value of greatest item in arr
        # constraint: logm time * n items?
        
        # how to determine whether a given value is valid?
        # must be able to consume all bananas in h hours
        # if bin search the value, then it's logm * n if iterating the array

        # solution:
        # bin search on hours to completion
        # track current candidate, hone in until value just below it is insufficient
        
        rate = 0
        lower_bound = 1
        upper_bound = max(piles)

        # bin search on hours to completion
        i = 0
        while i < 50:
            bph = (lower_bound + upper_bound) // 2
            hours = hoursUntilCompletion(bph, piles)
            
            if hours > h:
                # search higher bph
                lower_bound = bph + 1
            elif hours <= h:
                if bph == 1 or hoursUntilCompletion(bph - 1, piles) > h:
                    return bph
                else:
                    # can optimize for lower bph
                    upper_bound = bph - 1
            i += 1
        
        #    [ 3, 6, 7, 11 ] h = 8
        #     lower = 3
        #     upper = 4
        #     bph = 2
        #     hours = 8


def hoursUntilCompletion(bph, piles):
    hours = 0
    for i in range(len(piles)):
        hours += piles[i] // bph
        if piles[i] % bph != 0:
            hours += 1
    return hours
    
     