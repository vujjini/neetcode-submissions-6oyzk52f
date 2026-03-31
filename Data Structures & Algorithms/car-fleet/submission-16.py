class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse = True)

        st = []

        for currPos, currSpeed in cars:
            currTime = (target - currPos) / currSpeed
            if st and st[-1] >= currTime:
                continue
            st.append(currTime)
        
        return len(st)
        
