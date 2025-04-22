class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.frequency = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        self.size += 1
    
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1
    
    def removeTail(self):
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.freq = defaultdict(DLL)
        self.capacity = capacity
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.updateCache(self.cache[key], key, self.cache[key].val)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        
        if key in self.cache:
            self.updateCache(self.cache[key], key, value)
        else:
            if len(self.cache) == self.capacity:
                prevTail = self.freq[self.minFreq].removeTail()
                del self.cache[prevTail.key]
            node = Node(key, value)
            self.freq[1].insert(node)
            self.cache[key] = node
            self.minFreq = 1
    
    def updateCache(self, node, key, value):
        node = self.cache[key]
        node.val = value

        self.freq[node.frequency].remove(node)
        if self.minFreq == node.frequency and self.freq[node.frequency].size == 0:
            self.minFreq += 1

        node.frequency += 1
        self.freq[node.frequency].insert(node)




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)