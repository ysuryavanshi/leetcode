class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        can_win = [1] * n
        for _, v in edges:
            can_win[v] = 0
        
        ans = None
        c = 0
        for i in range(n):
            if can_win[i] == 1:
                if c == 0:
                    ans = i
                    c = 1
                else:
                    return -1
        return ans