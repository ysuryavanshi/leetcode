class RandomizedSet:

    def __init__(self):
        self.data = []
        self.data_map = {}

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        last_element = self.data[-1]
        idx_val = self.data_map[val]

        self.data_map[last_element] = idx_val
        self.data[idx_val] = last_element

        self.data[-1] = val
        _ = self.data.pop()
        self.data_map.pop(val)
        return True


    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()