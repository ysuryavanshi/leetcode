class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans, cur = [], ''
        for c in searchWord:
            cur += c
            i = bisect_left(products, cur)
            ans.append([w for w in products[i: i+3] if w.startswith(cur)])
        return ans