class RandomizedSet:

    def __init__(self):
        self.rset = set()

    def insert(self, val: int) -> bool:
        if val not in self.rset:
            self.rset.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.rset:
            self.rset.discard(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.sample(tuple(self.rset), 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()