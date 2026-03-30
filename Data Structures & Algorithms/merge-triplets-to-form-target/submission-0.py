class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # start with [0, 0, 0]
        # consider the element if and only if all elements are <= target elements
        # at the end of traversal return curr == target

        curr = [0, 0, 0]
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                curr = [max(triplet[0], curr[0]), max(triplet[1], curr[1]), max(triplet[2], curr[2])]
        print(curr)
        return curr == target