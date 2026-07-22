class Solution:
    # Sort all cars into priority queue by position (descending)
    # While priority queue not empty (start with top item in queue):
    #   While previous fleet can merge:
    #      merge
    #   pop
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        num_fleets = 1
        last = None

        for i in range(len(position)):
            fleets.append((position[i], (get_ttd(target, position[i], speed[i]))))
        fleets.sort()

        while len(fleets) > 1:
            while fleets[-1][1] >= fleets[-2][1]:
                prev_arrival = fleets.pop()
                fleets[-1] = prev_arrival
                if len(fleets) == 1:
                    return num_fleets
            num_fleets += 1
            fleets.pop()

        return num_fleets

def get_ttd(target: int, position: int, speed: int):
    return (target - position) / speed
        # target = 10
        # [4, 1, 0, 7, 3] speed [2, 2, 1, 1, 1]

        # [(-7, 1), (-4, 2), (-3, 1), (-1, 2), (0, 1)]
        # [(-7, 1), (-3, 1), (-1, 2), (0, 1)]
        # [(-3, 1), (-1, 2), (0, 1)]                        num_fleets 2
        # [(-3, 1), (0, 1)]                                 num_fleets 2
        # [(0, 1)]                                          num_fleets 3

        # when will car p7 reach the destination? -> 3 hours
        # when will car p0 reach the destination? -> 

        # p7 -> 3 hrs
        # p0 -> 10 hrs
        # p1 -> 4.5 hrs
        # p4 -> 3 hrs
        # p3 -> 7 hrs

        # are any of the cars behind the current one going to reach the destination before this car?
        # - merge them to fleet and take the minimum speed (leaders speed)

        # think of cars as fleets rather than individuals

        # priority queue?

        # [p0 -> 10hrs], [p1 -> 4.5 hrs], [p3 -> 7 hrs], [p4 -> 3 hrs], [p7 -> 3hrs]
        # [p0 -> 10hrs], [p1 -> 4.5 hrs], [p3 -> 7 hrs], [pX -> 3hrs]
        # [p0 -> 10hrs], [pY -> 7 hrs], [pX -> 3hrs]