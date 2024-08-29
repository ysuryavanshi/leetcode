class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        def remove_point(a, b):
            points.discard((a, b))
            for y in x_dict[a]:
                if (a, y) in points: remove_point(a, y)

            for x in y_dict[b]:
                if (x, b) in points: remove_point(x, b)

        points = {(x, y) for x, y in stones}
        x_dict = defaultdict(list)
        y_dict = defaultdict(list)

        for x, y in stones:
            x_dict[x].append(y)
            y_dict[y].append(x)
        
        count = 0
        for x, y in stones:
            if (x, y) in points:
                remove_point(x, y)
                count += 1

        return len(stones) - count