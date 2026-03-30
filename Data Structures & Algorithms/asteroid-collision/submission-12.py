class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = [asteroids[0]]

        for i in range(1, len(asteroids)):
            if asteroids[i] > 0:
                st.append(asteroids[i])
            else:
                equal = False
                while st and st[-1] > 0 and abs(asteroids[i]) >= st[-1]:
                    top = st[-1]
                    st.pop()
                    if abs(asteroids[i]) == top:
                        equal = True
                        break
                if (not st or st[-1] < 0) and not equal:
                    st.append(asteroids[i])
                    
        
        return st