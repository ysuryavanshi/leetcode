class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_intervals = []
        y_intervals = []
        
        for x1, y1, x2, y2 in rectangles:
            x_intervals.append((x1, x2))
            y_intervals.append((y1, y2))

        x_intervals.sort()
        y_intervals.sort()
        
        end = gap = 0
        for x1, x2 in x_intervals:
            if not end:
                end = x2
                continue
            
            if x1 >= end:
                end = x2
                gap += 1
            else:
                end = max(end, x2)
        
        if gap >= 2:
            return True

        end = gap = 0
        for y1, y2 in y_intervals:
            if not end:
                end = y2
                continue
            
            if y1 >= end:
                end = y2
                gap += 1
            else:
                end = max(end, y2)
        return gap >= 2