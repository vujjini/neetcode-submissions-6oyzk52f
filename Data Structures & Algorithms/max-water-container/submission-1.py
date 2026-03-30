class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        # j = 1
        # max_area = min(heights[i], heights[j])
        # j+=1
        # while (j < len(heights)):
        #     curr_area = min(heights[i], heights[j])*(j - i)
        #     # max_area = max(max_area, curr_area)
        j = len(heights) - 1
        max_area = min(heights[i], heights[j])*(j - i)
        while i < j:
            max_area = max(max_area, min(heights[i], heights[j])*(j - i))
            if heights[i] < heights[j]:
                i+=1
                continue
            j-=1

        return max_area
        
                