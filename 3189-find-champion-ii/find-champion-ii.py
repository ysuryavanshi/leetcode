class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        can_win = [1] * n
        for _, v in edges:
            can_win[v] = 0
        
        if sum(can_win) > 1:
            return -1
        return can_win.index(1)