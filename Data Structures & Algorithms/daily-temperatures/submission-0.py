class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # cannot determine value corresponding to ith value until later value -> stack
        # iterate list. for each:
        #   while stack top lower temp than current, resolve
        #   push temp and list idx to stack
        stack = []
        days_till_warmer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                day = stack.pop()
                days_till_warmer[day[1]] = i - day[1]
            
            stack.append((temperatures[i], i))

        return days_till_warmer

        # (30, 0) (38,1) (30, 2) (36, 3)

        # (38, 1) (36, 3) (35, 4)

        # 1, 4, 1, 2, 1,
