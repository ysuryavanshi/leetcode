class Node:
    def __init__(self, key, val, previous=None, nxt=None):
        self.key = key
        self.val = val
        self.previous = previous
        self.next = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.cur_capacity = 0
        self.lookup = dict()

        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        node = self.lookup[key]
        node.previous.next = node.next
        node.next.previous = node.previous

        node.previous = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.previous = node
        
        return node.val
    
    def evict(self):
        del self.lookup[self.tail.previous.key]
        self.cur_capacity -= 1

        node = self.tail.previous
        node.previous.next = self.tail
        self.tail.previous = node.previous
        
        node.previous = node.next = None

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            _ = self.get(key)
            self.lookup[key].val = value
            return None

        if self.cur_capacity == self.max_capacity:
            self.evict()

        node = Node(key, value, self.head, self.head.next)
        self.lookup[key] = node
        self.head.next.previous = node
        self.head.next = node
        self.cur_capacity += 1

        return None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)