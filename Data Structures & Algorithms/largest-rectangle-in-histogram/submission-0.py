class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # brute force:
            # for each element -> expand to the left and right until the num <= the num being explored
            # record the max area = max(curr_max, the num * recorded_width)
        
        # if the top of the stack < num being added: push the number with starting point as its index
        # else: pop the top and set the starting point of new number = starting point of popped number
                # calculate the max area of the recatngle formed with popped element: 

        # [7, 1]

        # [1, 0]

        # [(1, 0), (7, 0)]

        # area of popped height = 7*(i - starting_point)

        res = 0
        st = []
        n = len(heights)

        for i in range(len(heights)):
            starting = i
            while st and st[-1][0] >= heights[i]:
                height, starting = st.pop()
                res = max(res, height*(i - starting))
            st.append((heights[i], starting))
        
        for height, starting in st:
            res = max(res, height*(n - starting))
        
        return res