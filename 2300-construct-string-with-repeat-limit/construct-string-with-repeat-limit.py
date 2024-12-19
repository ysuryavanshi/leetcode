class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        h = [(-ord(k), v) for k, v in count.items()]
        heapify(h)

        res = ''
        while h:
            count = 0
            c, times = heapq.heappop(h)
            c = chr(-c)
            
            if res and c == res[-1]:
                if not h:
                    break
                temp = heapq.heappop(h)
                (c, times), temp = temp, (-ord(c), times)
                c = chr(-c)
                heapq.heappush(h, temp)  
                res += c
                times -= 1
                if times > 0:
                    heapq.heappush(h, (-ord(c), times))
            elif times <= repeatLimit:
                res += c * times
            else:
                res += c * repeatLimit
                heapq.heappush(h, (-ord(c), times - repeatLimit))

        return res
        