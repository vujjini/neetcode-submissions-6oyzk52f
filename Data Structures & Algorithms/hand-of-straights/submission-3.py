class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # maintain a minHeap stores -> (digit, count (nonzero))
        # a temp list to push back into the minHeap after group loop is finished
        # if in middle of the group loop, if the currNum != prevNum + 1 return False

        minHeap = []
        counts = Counter(hand)

        for card in counts:
            heapq.heappush(minHeap, [card, counts[card]])

        # [(2, 1), (3, 1), (4, 1), (5, 1)]
        # []

        while minHeap:
            tmp = []
            top = heapq.heappop(minHeap)
            top[1]-=1
            if top[1] > 0:
                tmp.append(top)
            prevCard = top[0]
            for _ in range(groupSize - 1):
                if not minHeap:
                    return False
                nextCard = heapq.heappop(minHeap)
                if nextCard[0] != prevCard + 1:
                    return False
                nextCard[1]-=1
                if nextCard[1] > 0:
                    tmp.append(nextCard)
                prevCard = nextCard[0]
            print(tmp)
            for newCard in tmp:
                heapq.heappush(minHeap, newCard)
        
        return True

        