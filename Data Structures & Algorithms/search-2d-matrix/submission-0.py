class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # have two pointers low and high for the first two rows
        # if target > middle row[0]
            # if target < middle row[-1], the target is in current row
                # set low to middle row[0] and high to middle row[-1]
                # do binary search here
            # else:
                # move low to middle row
        # else if target < middle row[0]:
            # move high to middle row
        # else, target found
        low = 0
        high = len(matrix) - 1
        while low <= high:
            middle_index = (high + low) // 2
            middle_row = matrix[middle_index]
            if target > middle_row[0]:
                if target < middle_row[-1]:
                    i = 0
                    j = len(middle_row) - 1
                    while (i <= j):
                        mid = (i + j) // 2
                        if target < middle_row[mid]:
                            j = mid - 1
                        elif target > middle_row[mid]:
                            i = mid + 1
                        else:
                            return True
                    return False
                elif target == middle_row[-1]:
                    return True
                else:
                    low = middle_index + 1
            elif target < middle_row[0]:
                high = middle_index - 1
            else:
                return True
        return False

                
                    

