class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.capacity = 0
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.capacity < self.k:
            if self.capacity == 0:
                self.front = Node(value)
                self.rear = self.front
                self.rear.next = self.front
                self.front.next = self.rear
            else:
                newNode = Node(value)
                self.rear.next = newNode
                self.rear = newNode
                self.rear.next = self.front
            self.capacity+=1
            return True
        return False

    def deQueue(self) -> bool:
        if self.capacity > 0:
            if self.capacity == 1:
                self.front = None
                self.rear = None
            else:
                self.rear.next = self.front.next
                self.front = self.rear.next
            self.capacity-=1
            return True
        return False

    def Front(self) -> int:
        return self.front.val if self.front else -1

    def Rear(self) -> int:
        return self.rear.val if self.rear else -1

    def isEmpty(self) -> bool:
        return not self.front

    def isFull(self) -> bool:
        return self.capacity == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()