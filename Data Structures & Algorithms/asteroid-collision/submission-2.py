class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        include = [True]*len(asteroids)
        st = []

        i = len(asteroids) - 1
        while i >= 0:
            if asteroids[i] < 0:
                st.append(i)
                i-=1
            else:
                if not st:
                    i-=1
                elif -(asteroids[st[-1]]) > asteroids[i]:
                    include[i] = False
                    i-=1
                elif -(asteroids[st[-1]]) == asteroids[i]:
                    include[i] = False
                    include[st[-1]] = False
                    st.pop()
                    i-=1
                else:
                    include[st[-1]] = False
                    st.pop()
        
        res = []
        for i in range(len(include)):
            if include[i]:
                res.append(asteroids[i])
        
        return res

