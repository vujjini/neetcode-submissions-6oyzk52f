class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # find the minimum weight (>= max weight) that satisfies
        # the condition (max days) -> checking for the condition takes
        # O(n). Finding the mim weight takes O(logn)
        # sort the list at beginning for easier checking of condition

        # weights.sort()

        def isSatisfied(capacity):
            curr_sum = 0
            curr_days = 1
            for i in weights:
                if curr_sum > capacity: 
                    return False
                if curr_sum + i <= capacity:
                    curr_sum+=i
                else:
                    curr_sum = i
                    curr_days+=1
            
            return curr_days <= days 
        max_weight = sum(weights)
        left = max(weights)
        right = max_weight
        res = max_weight
        while left <= right:
            mid = (right + left) // 2
            if isSatisfied(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res
            