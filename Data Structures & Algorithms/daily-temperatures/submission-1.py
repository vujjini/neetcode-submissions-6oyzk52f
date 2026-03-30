class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force: O(n^2)
        # res = [0]*n; n = length of list
        # stack of tuples. each tuple has element number and index
        # iterate through the list using index
        # for each element, we compare that element to the
        # top element in the stack.
            # if greater than or equal to: we calculate the diff between their indices and
                # update the element at that position in res with index difference
                # remove the element from the stack.
                # add the current element to the stack
            # else:
                # add the current element to the stack
            # base case:
                # if first element, just add it to that stack
        n = len(temperatures)
        res = [0]*n
        st = []
        for i in range(n):
            if len(st) > 0 and temperatures[i] > st[-1][0]:
                diff = i - st[-1][1]
                res[st[-1][1]] = diff
                st.pop()
                while(len(st) > 0 and temperatures[i] > st[-1][0]):
                    diff = i - st[-1][1]
                    res[st[-1][1]] = diff
                    st.pop()
            st.append((temperatures[i], i))
        
        return res




