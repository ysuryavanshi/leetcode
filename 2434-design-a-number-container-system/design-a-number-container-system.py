class NumberContainers:

    def __init__(self):
        self.index_num = {}
        self.num_index = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.index_num:
            old_num = self.index_num[index]

            old_num_pos = bisect_left(self.num_index[old_num], index)
            self.num_index[old_num].pop(old_num_pos)
            if not self.num_index[old_num]:
                del self.num_index[old_num]

        new_num_pos = bisect_left(self.num_index[number], index)
        self.num_index[number].insert(new_num_pos, index)
        self.index_num[index] = number

    def find(self, number: int) -> int:
        return self.num_index[number][0] if number in self.num_index else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)