class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if x <= arr[0]:
            return arr[:k]
        
        if x >= arr[-1]:
            return arr[len(arr) - k:]
        
        l = 0
        r = len(arr) - 1

        start = 0

        while l <= r:
            m = (l + r) // 2
            if arr[m] == x:
                start = m
                break
            elif arr[m] > x:
                r = m - 1
            else:
                start = m if arr[m] >= arr[start] else start
                l = m + 1
        
        i = start - k + 1 if start >= k - 1 else 0
        end = start + k if (start + k) < len(arr) else len(arr) - 1

        if (end - i + 1) <= k:
            return arr[i:end + 1]
        
        right = i + k

        while right <= end:
            if abs(arr[right] - x) >= abs(arr[i] - x):
                return arr[i:right]
            else:
                i+=1
                right+=1
        
        return arr[i:right]



        


