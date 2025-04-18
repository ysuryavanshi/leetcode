class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        visited = set()

        def backtrack(idx, num_list):
            if idx == n:
                res.append(num_list[:])
                return
            
            for i in range(n):
                if nums[i] in visited:
                    continue
                
                visited.add(nums[i])
                num_list.append(nums[i])

                backtrack(idx + 1, num_list)

                _ = num_list.pop()
                visited.remove(nums[i])
                
            return

        backtrack(0, [])
        return res