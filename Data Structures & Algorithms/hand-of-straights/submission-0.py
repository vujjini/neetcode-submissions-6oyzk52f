from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # {1:1, 2:1, 3: 2, ....}
        # while the heapq is not empty:
            # curr_min = heappop() and map[curr_min]-=1
            # for i in range(curr_min + 1, curr_min + groupsize)
                # check if i exists in the map
                # if it does, also do map[i]-=1 and do heappop() only if map[i] becomes 0
                # if it doesnt return False
        
        if len(hand)%groupSize != 0:
            return False
            
        m = Counter(hand)
        heapq.heapify(hand)

        while len(hand) != 0:
            curr_min = heapq.heappop(hand)
            m[curr_min]-=1
            if m[curr_min] == 0:
                del m[curr_min]
                while len(hand) > 0 and hand[0] == curr_min:
                    heapq.heappop(hand)
            print(hand)
            for i in range(curr_min + 1, curr_min + groupSize):
                if i in m:
                    m[i]-=1
                    if m[i] == 0:
                        del m[i]
                        while len(hand) > 0 and hand[0] == i:
                            heapq.heappop(hand)
                else:
                    return False
        
        return True