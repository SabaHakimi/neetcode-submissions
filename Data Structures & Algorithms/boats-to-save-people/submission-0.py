class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1

        people.sort()
        l = 0
        r = len(people) - 1
        num_boats = 0

        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            num_boats += 1
        if l == r:
            num_boats += 1
        
        return num_boats

            