class Solution:
    def countAndSay(self, n: int) -> str:
        sequence = '1'

        for _ in range(n - 1):
            pairs = []
            last_char = None
            count = 0

            for c in sequence:
                if not last_char:
                    last_char = c
                    count = 1
                elif last_char != c:
                    pairs.append([str(count), last_char])
                    last_char = c
                    count = 1
                else:
                    count += 1
            pairs.append([str(count), last_char])    
            sequence = ''.join([''.join(i) for i in pairs])

        return sequence
