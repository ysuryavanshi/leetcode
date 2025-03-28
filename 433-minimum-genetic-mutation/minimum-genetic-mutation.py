class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        q = deque([startGene])
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                gene = list(q.popleft())
                for i, temp in enumerate(gene):
                    for c in 'ACGT':
                        gene[i] = c
                        gene_str = ''.join(gene)
                        if gene_str == endGene:
                            return res
                        elif gene_str in bank:
                            q.append(gene_str)
                            bank.remove(gene_str)
                    gene[i] = temp
        
        return -1