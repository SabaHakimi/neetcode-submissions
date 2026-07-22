class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # unordered
        # catching up if prev would reach target at some time as current or sooner
        # always compare top 2 each time stack is updated
        # care about time to destination -> if prev ttd <= current, merge

        #- sort pairs of of position and speed but only by position 
        #- only keep track of each fleet's TTD for comparisons
        #- iterate over list of pos, speed pairs from highest pos to lowest and for each item, call it 'current item' 
        #- each time item is being considered/'current', compare ttd with the bottleneck's ttd
        #  if current item ttd is less than or equal to, consider it merged and go to next item
        #  else, increment num fleets and set bottleneck to current item, then go to next item
        #- when done iterating, return num fleets
        
        # Pair positions and speeds, sort by pos descending 
        pns = [0] * len(position)
        for i in range(len(position)):
            pns[i] = (position[i], speed[i])
        pns.sort(reverse=True)
        print(pns)
        

        # compare vals
        bottleneck = getTTD(target, pns[0][0], pns[0][1])
        num_fleets = 1

        for i in range(len(pns)):
            ttd = getTTD(target, pns[i][0], pns[i][1])
            if ttd > bottleneck:
                num_fleets += 1
                bottleneck = ttd


        
        return num_fleets


def getTTD(target, pos, speed):
    remaining_dist = target - pos
    ttd = remaining_dist / speed
    return ttd
            

        

  


        # 3, 6, 6, 5

        # 10 - 7 = 3 -> 3 / 1 = 3
        # 10 - 2 = 8 -> 8 / 3 =  2.6 -> 3





        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]

        # Output: 3

        # sorted: [7, 4, 1, 0] and [1, 1, 3, 2]



        # (7, 1), (4, 1), (1, 3)
        # 3 hrs, 6 hrs, 3 hrs, -> 3 hrs, 6 hrs -> 3 hrs, 6 hrs, 5 hrs -> 3 hrs, 6 hrs