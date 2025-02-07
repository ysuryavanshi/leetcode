class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_count = defaultdict(int)
        ball_color = {}
        
        res = []
        for ball, color in queries:
            if ball in ball_color:
                if color_count[ball_color[ball]] == 1:
                    del color_count[ball_color[ball]]
                else:
                    color_count[ball_color[ball]] -= 1
                color_count[color] += 1
            else:
                color_count[color] += 1
            ball_color[ball] = color

            res.append(len(color_count))
        return res