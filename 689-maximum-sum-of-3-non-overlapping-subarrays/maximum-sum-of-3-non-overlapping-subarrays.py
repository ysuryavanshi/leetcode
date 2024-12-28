class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        p_sum = [sum(nums[:k])]
        for i in range(k, n):
            p_sum.append(p_sum[-1] + nums[i] - nums[i - k])

        dp = {}
        def helper(i, count_s_arr):
            if count_s_arr == 3 or i > n - k:
                return 0
            if (i, count_s_arr) in dp:
                return dp[(i, count_s_arr)]

            skip = helper(i + 1, count_s_arr)
            include = p_sum[i] + helper(i + k, count_s_arr + 1)

            dp[(i, count_s_arr)] = max(skip, include)

            return dp[(i, count_s_arr)]

        def get_index():
            i = 0
            res = []

            while i <= n - k and len(res) < 3:
                include = p_sum[i] + helper(i + k, len(res) + 1)
                skip = helper(i + 1, len(res))

                if include >= skip:
                    res.append(i)
                    i += k
                else:
                    i += 1
            return res

        return get_index()