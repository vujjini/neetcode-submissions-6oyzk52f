class Solution:
    def trap(self, height: List[int]) -> int:
        
        # at each point, get max height l to the left > curr point and max height to the right r > curr point
        # and get the water that can be stored at that point
        # by computing min(r, l) - height at that point
        # add up all of them

        res = 0

        leftMax = [height[i] for i in range(len(height))]
        rightMax = [height[i] for i in range(len(height))]

        maxLeft = float('-inf')
        maxRight = float('-inf')

        for i in range(len(height)):
            maxLeft = max(maxLeft, height[i])
            leftMax[i] = maxLeft
            maxRight = max(maxRight, height[len(height) - i - 1])
            rightMax[len(height) - i - 1] = maxRight

        for i in range(len(height)):
            
            res+=(min(leftMax[i], rightMax[i]) - height[i])


        return res
