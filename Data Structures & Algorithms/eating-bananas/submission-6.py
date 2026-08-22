import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [ 1 2 3 4 5 ] 7 lim, rate = 3
        # must eat all in h hrs
        # search space is rate at which to eat bananas
        # min is 1
        # max is max value in array
        # want to find the smallest value that satisfies h
        # connection between k and h
        # want O(nlogm) time and O(1) space
        # invariant: if chosen k satisifes h, and chosen k + 1 does not, return k
        # if do not satisfy h, search higher
        # if satisfy h, search lower
        # repeat until search space exhausted, keeping track of best valid k

        # [1,4,3,2], h = 9
        # l = 1
        # h = 4
        # m = 2 -> satisfy h

        # h = 1
        # l = 1
        # m = 1

        # Initialize search bounds
        lower = 1
        upper = max(piles)
        best = upper

        # Search
        while lower <= upper:
            k = (lower + upper) // 2
            # Determine if chosen k satisfies h
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / k)
            
            # If valid k, update best and search lower
            if hours_spent <= h:
                if k < best:
                    best = k
                upper = k - 1
            # If invalid, search higher
            elif hours_spent > h:
                lower = k + 1
                
        return best


            