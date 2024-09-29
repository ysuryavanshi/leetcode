class DoubleLinkedList:
    def __init__(self, value, nxt, previous):
        self.value = value
        self.next = nxt
        self.previous = previous


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_length = k        

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        if self.head is None:
            self.head = DoubleLinkedList(value, None, None)
            self.tail = self.head
        else:
            new = DoubleLinkedList(value, self.head, None)
            self.head.previous = new
            self.head = new
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        if self.tail is None:
            self.tail = DoubleLinkedList(value, None, None)
            self.head = self.tail
        else:
            new = DoubleLinkedList(value, None, self.tail)
            self.tail.next = new
            self.tail = new
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
        
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.value

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.value

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return self.size == self.max_length


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()