class Solution:
    def trap(self, height: List[int]) -> int:
        
        # at each point, get max height l to the left > curr point and max height to the right r > curr point
        # and get the water that can be stored at that point
        # by computing min(r, l) - height at that point
        # add up all of them

        res = 0

        for i in range(len(height)):
            maxLeft = height[i]
            maxRight = height[i]

            l = i - 1
            r = i + 1

            while l >= 0:
                maxLeft = max(maxLeft, height[l])
                l-=1
           
            while r < len(height):
                maxRight = max(maxRight, height[r])
                r+=1
            
            res+=(min(maxLeft, maxRight) - height[i])


        return res
