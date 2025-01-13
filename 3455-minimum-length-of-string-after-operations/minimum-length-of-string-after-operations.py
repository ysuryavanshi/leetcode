class Solution:
    def minimumLength(self, s: str) -> int:
    	count = Counter(s)

    	res = 0
    	for _, value in count.items():
    		res += 1 if value % 2 else 2

    	return res