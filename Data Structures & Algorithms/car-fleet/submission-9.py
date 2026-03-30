class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first sort times
        # length of set of the sorted times gives a rough answer
        times = [(position[i], (target - position[i])/speed[i]) for i in range(len(speed))]
        times.sort(key=lambda tup: tup[0], reverse=True)

        # create n = no of fleets (1 by default)
        # loop thru times from the second one
        # if same as before one, continue
        # else:
            # if position is greater than or equal to before, continue
            # else n+=1
        print(times)
        n = 1
        prev_time = times[0][1]
        for i in range(1, len(times)):
            if times[i][1] <= prev_time:
                continue
            else:
                n+=1
                prev_time = times[i][1]

        
        return n