class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []

        for a, b, c, d in rects:
            area = (c - a + 1) * (d - b + 1)
            self.weights.append(area)

    def pick(self) -> List[int]:
        r = random.choices(self.rects, self.weights, k=1)[0]
        return randint(r[0], r[2]), randint(r[1], r[3])



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()