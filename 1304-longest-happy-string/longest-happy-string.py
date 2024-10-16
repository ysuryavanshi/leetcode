class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        queue = []
        if a > 0: heappush(queue, (-a, 'a'))
        if b > 0: heappush(queue, (-b, 'b'))
        if c > 0: heappush(queue, (-c, 'c'))

        ans = []
        while queue:
            count1, char1 = heappop(queue)
            if len(ans) >= 2 and ans[-2:] == [char1, char1]:
                if not queue: break
                count2, char2 = heappop(queue)
                ans.append(char2)
                count2 += 1
                if count2 < 0: heappush(queue, (count2, char2))
                heappush(queue, (count1, char1))
            else:
                ans.append(char1)
                count1 += 1
                if count1 < 0: heappush(queue, (count1, char1))
        return ''.join(ans)