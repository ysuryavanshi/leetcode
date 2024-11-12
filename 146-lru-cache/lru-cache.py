class LRUCache:

    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.data:
            return self.data.setdefault(key, self.data.pop(key))
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key)
            self.data[key] = value
        else:
            self.data[key] = value
            if len(self.data) > self.capacity:
                self.data.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)